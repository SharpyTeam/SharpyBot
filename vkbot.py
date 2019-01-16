from flask import Flask, request, json
from settings import *
from logics import process_command

import random
import re
import vk

app = Flask(__name__)

session = vk.Session()
api = vk.API(session, v = '5.92')

@app.route('/', methods = ['POST'])
def processing():
    data = json.loads(request.data)
    if 'type' not in data.keys():
        return 'not vk'
    if data['type'] == 'confirmation':
        return confirmation_token
    elif data['type'] == 'message_new':
        c_id =  (data['object']['peer_id'] - 2000000000)
        params = process_command(data['object']['text']) 
        if (params is not None):
            api.messages.send(access_token = token, chat_id = c_id, random_id = random.randint(0, 2147483647), **params)
        return 'ok'