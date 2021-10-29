import requests

class Client:
    def __init__(self, URL):
        self.sessionCreated = requests.Session()
        response = self.sessionCreated.get(URL)
        
    def set_header(self,key,value):
        self.sessionCreated.headers.update({key:value})

    def get_response(self, URL):
        response = self.sessionCreated.get(URL)
        print("response status : "+str(response.status_code))
        if(response is not None):
            print('ok')

        if response.status_code == 200:
            return response.text
        else:
            return None

    def __del__(self):
        self.sessionCreated.close()


client = Client('https://httpbin.org')
client.set_header('user-agent','test_client')
response = client.get_response('https://httpbin.org')
print(response)






