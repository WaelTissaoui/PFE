import requests
import json
FACEBOOK_GRAPH_URL ='https://graph.facebook.com/v6.0/me/messages?access_token=EAAClwHPhABYBAOj18Os6ItFWnAgPMflwik8pd4i2gFfybE6ixCVaR8n2Hvc9SbdBSwXMzNAQJIuTPQ6bQtOvx16Wo968GOhfbV70Nn25h3JQpsIyyopukydbhSZAk27scXhXVAGEzA3AjImbwLKG66jZBTZBZAAgsP6i3wZATmYShL4heLQJL'



class Bot(object):
    def __init__(self,access_token,api_url=FACEBOOK_GRAPH_URL):
        self.access_token = access_token
        self.api_url = api_url
    

    def send_text_message(self,psid,message,messaging_type="RESPONSE"):
        headers = {
            'Content-Type':'application/json'

        }
        type='text'
        data = {
            'messaging_type': messaging_type,
            'recipient':{'id':psid},
            'message' :{type:message}
        }
        params={'access_token': self.access_token}
        self.api_url = self.api_url+'messages'
        response = requests.post(self.api_url,headers=headers,params=params,data=json.dumps(data)) 
        print(response.content)


