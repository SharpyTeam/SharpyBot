import random
import subprocess

import vk
from flask import Flask, request, json

from logics import process_message
from settings import *

app = Flask(__name__)

session = vk.Session()
api = vk.API(session, v='5.92')


@app.route('/', methods=['POST'])
def processing():
    data = json.loads(request.data)
    if 'type' not in data.keys():
        return 'not vk'
    if data['type'] == 'confirmation':
        return confirmation_token
    elif data['type'] == 'message_new':
        if 'secret' not in data or data['secret'] != secret_token:
            return 'ok'

        params = process_message(data['object']['text'])

        if params is not None:
            print("Received appropriate message with trigger.")
            print("Callback object:")
            print(repr(data))
            api.messages.send(access_token=token, peer_id=data['object']['peer_id'],
                              forward_messages=str(data['object']['conversation_message_id']),
                              random_id=random.randint(0, 2147483647), **params)
    return 'ok'


@app.route('/repo_push', methods=['POST'])
def repo_push():
    print("Repository has been updated, fetching it again...")
    # hardcoded, but i do not give a shit
    subprocess.run(["git", "fetch", "--all"], cwd='/home/selya/vkbot')
    subprocess.run(["git", "reset", "--hard", "origin/master"], cwd='/home/selya/vkbot')
    subprocess.run(["touch", "/var/www/selya_pythonanywhere_com_wsgi.py"])
    return 'ok'
