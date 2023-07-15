import os
import socket
import sys
import datetime
import contextlib
from myserve import MyServe
import threading
#--------------------------------------------------------------
""""""
    

        
class HttpServer:
    HOST='0.0.0.0'
    PORT=55555
    def __init__(self):
        pass
    def run(self):
        if len(sys.argv)== 2:
            try:
                PORT=int(sys.argv[1])
                self.PORT=PORT
            except:
                print("Port value must be an integer") 
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            
            server_socket.bind(("0.0.0.0", self.PORT))
            server_socket.listen(5)
            print("Myserver: {0}:{1}".format("0.0.0.0", self.PORT))
            while True:
                print("Myserver is listening.......")
                sock, addr= server_socket.accept()
                print("Connection established for {0}".format(addr))
                with contextlib.closing(sock) as sock:
                    serve= MyServe(sock, self.HOST,self.PORT)
                    serve.start()
                    serve.join()
                    print(serve.getName())
         
if __name__=="__main__":
    server=HttpServer()
    server.run()


        
     
            
        
        