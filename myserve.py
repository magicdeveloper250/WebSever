from threading import Thread
import threading
import os
import socket
from requesthandler import RequestHandler
import datetime

class MyServe(Thread):
    def __init__(self, client:socket.socket(), host, port):
        threading.Thread.__init__(self)
        self.HOST=host
        self.PORT=port
        self.client = client
        self.request= None
    def get_http_response_header(self, resource:str):
        resource_pre="text"
        resource_type="html"
        if resource.endswith("ico"):
            resource_pre="image"
            resource_type= "ico"
        header="HTTP/1.1 200 OK\r\n"
        header+="Date: {0}\r\n".format(datetime.datetime.now().date())
        header+="Server: {0}:{1}\r\n".format(self.HOST, self.PORT)
        header+=f"Content-Type: {resource_pre}/{resource_type}\r\n"
        header+="\n"
        return header
    def get_request(self):
        client_socket=self.client
        client_socket= self.client
        flo= client_socket.makefile(mode="r", encoding="utf-8")
        request_handler=RequestHandler()
        raw_request= request_handler.validate_request(flo)
        #print(raw_request)
        try:
            request=raw_request[0].split()
            self.request=request
        except IndexError:
            print("no data provided by client")

        
    def provide_response(self):
        client_socket= self.client
         
        filename=""
        if len(self.request)<2:
            flo= client_socket.makefile(mode="w", encoding="iso-8859-1")
            path="badrequest.html"
            with open(path, "r") as file:
                flo.writelines(file.readlines())
            print("bad request received from client")
            flo.flush()

        try:
            if self.request[1].startswith("/?"):
                
                request_handler=RequestHandler()
                self.request= request_handler.validate_form_request(self.request[1])
                print(self.request)
                
                if "response.html" in os.listdir():
                    os.remove("response.html")
                args= str(self.request)
                os.system(f"python response.py {args}>>response.html")
                filename="response.html"
            else: 
                request_type= self.request[0]
                filename= self.request[1]
        except TypeError: # raised if client no data sent to server
            print("no data provided by client")
        except KeyError:
            print("no data provided by client ")
       
        if filename=="/":
            filename="index.html"
        path= os.path.join("{0}".format(filename).replace("/",""))
        flo= client_socket.makefile(mode="w", encoding="iso-8859-1")

        header= self.get_http_response_header(filename)
        print(header)
        
        try:
            flo.write(header)
            with open(path, "r") as file:
                flo.writelines(file.readlines())
        # if requested file not found on server bring not found error page
        except FileNotFoundError:
            path="notfound.html"
            with open(path, "r") as file:
                flo.writelines(file.readlines())
            print("{0} not found".format(filename))
        try:

            flo.flush()
            print("Requested resources brought to client.\n")
        except OSError as ex:
            pass



    def run(self):
        self.get_request()
        self.provide_response()


