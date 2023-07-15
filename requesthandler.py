class RequestHandler:
    def __init__(self):
        # request form GET FILENAME HTTP/1.1 \n Host: HOST\n content-type
        pass
    
    def validate_request(self,request:str):
        full=[]
        for char in request:
            full.append(char.rstrip().strip())
            if char=="\n":
                break
        return full
    def validate_form_request(self, request:str):
        print(request)
        #new_request="".join(request)
        new_request= request
        new_request=new_request.replace("/","")
        new_request=new_request.replace("?","")
        new_request=new_request.replace("+"," ")
        request_list=new_request.split("&")
        #print(request_list)
        args={}
        for arg in request_list:
            vals=arg.split("=")
            args[vals[0]]=vals[1]
            if arg=="":
                break
        print(args)
        return args
                    
        


         
    def __repr__(self):
        return self.request