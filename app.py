from flask import Flask, request
import json
import os
import datetime
from NLP.Chat_Bot import Bot
from response import response
PAGE_ACCESS_TOKEN='EAAClwHPhABYBAOj18Os6ItFWnAgPMflwik8pd4i2gFfybE6ixCVaR8n2Hvc9SbdBSwXMzNAQJIuTPQ6bQtOvx16Wo968GOhfbV70Nn25h3JQpsIyyopukydbhSZAk27scXhXVAGEzA3AjImbwLKG66jZBTZBZAAgsP6i3wZATmYShL4heLQJL'
app = Flask(__name__)
r=response("config.yaml","testData.json","./data/")
r.train()
bot = Bot(PAGE_ACCESS_TOKEN)
@app.route('/', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')
        if token == 'wael':
            return str(challenge)


        return '400'
    else:
        print(request.data)
        data = json.loads(request.data)
        messaging_events = data['entry'][0]['messaging']
        for message in messaging_events:
            user_id = message['sender']['id']
            text_input= message['message'].get('text')
            print('Message from user ID {} - {} '.format(user_id,text_input))
            return_message = r.reply(text_input)
            bot.send_text_message(user_id,return_message)
        return '200'

if __name__ == '__main__':
    


    app.run(debug=True)