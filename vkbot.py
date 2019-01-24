import random
import subprocess

import vk
from flask import Flask, request, json, render_template

import database
from logics import process_message
from settings import confirmation_token, token, secret_token

app = Flask(__name__)

session = vk.Session()
api = vk.API(session, v='5.92')

database.init()


@app.route('/', methods=['POST'])
def processing():
    data = json.loads(request.data)

    if 'type' not in data.keys():
        return 'not vk'

    if data['type'] == 'confirmation':
        return confirmation_token

    if data['type'] == 'message_new':
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


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/repo_push', methods=['POST'])
def repo_push():
    print("Repository has been updated, fetching it again...")
    # hardcoded, but i do not give a shit
    subprocess.run(["/usr/bin/git", "fetch", "--all"], cwd='/var/apps/sharpybot')
    subprocess.run(["/usr/bin/git", "reset", "--hard", "origin/master"], cwd='/var/apps/sharpybot')
    subprocess.run(["/usr/bin/touch", "_reload_wand"])
    return 'ok'
