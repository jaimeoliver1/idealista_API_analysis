import base64
import urllib
import requests
import json
import os

def get_oauth_token():
    url = "https://api.idealista.com/oauth/token"   
    apikey= os.getenv('idealista_apikey') # sent by idealista
    secret= os.getenv('idealista_pass')   # sent by idealista
    log = apikey + ':' + secret
    auth = base64.b64encode(log.encode()).decode()
    headers = {'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8' ,'Authorization' : 'Basic ' + auth}
    params = urllib.parse.urlencode({'grant_type':'client_credentials'})
    content = requests.post(url,headers = headers, params=params)
    bearer_token = json.loads(content.text)['access_token']
    return bearer_token

def search_api(token, url):  
    headers = {'Content-Type': 'Content-Type: multipart/form-data;', 'Authorization' : 'Bearer ' + token}
    content = requests.post(url, headers = headers)
    result = json.loads(content.text)
    return result

class IdealistaExtraction:
    
    def __init__(self, date):

        self.date = date
        
    def get_oauth_token(self):
        url = "https://api.idealista.com/oauth/token"    
        apikey= 'g42dt0w3gbc9yum232l5urd56w1ha3rq' #sent by idealista
        secret= '1tK3ipwQIhja'  #sent by idealista
        log = apikey + ':' + secret
        auth = base64.b64encode(log.encode()).decode()
        headers = {'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8' ,'Authorization' : 'Basic ' + auth}
        params = urllib.parse.urlencode({'grant_type':'client_credentials'})
        content = requests.post(url,headers = headers, params=params)
        bearer_token = json.loads(content.text)['access_token']
        return bearer_token

    def search_api(self, token, url):  
        headers = {'Content-Type': 'Content-Type: multipart/form-data;', 'Authorization' : 'Bearer ' + token}
        content = requests.post(url, headers = headers)
        result = json.loads(content.text)
        return result