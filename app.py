import vk
from flask import Flask, request, json

from config import confirmation_token, token, secret_token
import modules


# All commands listed in a list
print(modules.collect_commands())

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

    if data['type'] == 'message_new':
        if 'secret' not in data or data['secret'] != secret_token:
            return 'ok'
        # message processing here


    return 'ok'
