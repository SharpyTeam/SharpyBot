import random
import subprocess

from flask import json, request, render_template

from sharpy.config import confirmation_token, secret_token, token
from sharpy.logics import process_message
from . import main


@main.route('/', methods=['POST'])
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
            print(api.messages.getByConversationMessageId(
                access_token=token, peer_id=str(data['object']['peer_id']),
                group_id=data['group_id'],
                conversation_message_ids=str(data['object']['conversation_message_id'])
            ))
            api.messages.send(access_token=token, peer_id=data['object']['peer_id'],
                              forward_messages=str(data['object']['conversation_message_id']),
                              random_id=random.randint(0, 2147483647), **params)
    return 'ok'


@main.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@main.route('/repo_push', methods=['POST'])
def repo_push():
    print("Repository has been updated, fetching it again...")
    # hardcoded, but i do not give a shit
    subprocess.run(["/usr/bin/git", "fetch", "--all"], cwd='/var/apps/sharpybot')
    subprocess.run(["/usr/bin/git", "reset", "--hard", "origin/master"], cwd='/var/apps/sharpybot')
    subprocess.run(["/usr/bin/touch", "_reload_wand"])
    return 'ok'