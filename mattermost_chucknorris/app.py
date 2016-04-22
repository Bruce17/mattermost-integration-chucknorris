# -*- coding: utf-8 -*-
import logging
import os
import sys
import json
from urlparse import urlsplit
from urlparse import urlunsplit

import requests
from flask import Flask
from flask import request
from flask import Response

from mattermost_chucknorris.settings import *


logging.basicConfig(
    level=logging.INFO, format='[%(asctime)s] [%(levelname)s] %(message)s')
app = Flask(__name__)


@app.route('/')
def root():
    """
    Home handler
    """

    return "OK"

@app.route('/random', methods=['POST'])
def random():
    """
    Get a random Chuck Norris fact
    """

    try:
        resp_data = {}
        resp_data['username'] = USERNAME
        resp_data['icon_url'] = ICON_URL

        data = request.form

        if not 'token' in data:
            raise Exception('Missing necessary token in the post data')

        if MATTERMOST_CHUCK_NORRIS_TOKEN.find(data['token']) == -1:
            raise Exception('Tokens did not match, it is possible that this request came from somewhere other than Mattermost')

        # NOTE: support the slash command
        if 'command' in data:
            # slash_command = True
            resp_data['response_type'] = 'in_channel'

        resp_data['text'] = get_fact()
    except Exception as err:
        msg = err.message
        logging.error('unable to handle new post :: {}'.format(msg))
        resp_data['text'] = msg
    finally:
        resp = Response(content_type='application/json')
        resp.set_data(json.dumps(resp_data))
        return resp

@app.route('/new_fact', methods=['POST'])
def new_fact():
    """
    Get a Chuck Norris fact using a "firstname" & "lastname"
    """
    try:
        # NOTE: common stuff
        slash_command = False
        resp_data = {}
        resp_data['username'] = USERNAME
        resp_data['icon_url'] = ICON_URL

        data = request.form

        if not 'token' in data:
            raise Exception('Missing necessary token in the post data')

        if MATTERMOST_CHUCK_NORRIS_TOKEN.find(data['token']) == -1:
            raise Exception('Tokens did not match, it is possible that this request came from somewhere other than Mattermost')

        # NOTE: support the slash command
        if 'command' in data:
            # slash_command = True
            resp_data['response_type'] = 'in_channel'

        nameParts = data['text'].split(' ')

        if len(nameParts) <= 1:
            resp_data['text'] = get_fact()
        elif len(nameParts) == 2:
            resp_data['text'] = get_fact(firstname=nameParts[0], lastname=nameParts[1])
        elif len(nameParts) == 3:
            resp_data['text'] = get_fact(firstname=nameParts[0], lastname=nameParts[1], category=nameParts[2])
    except Exception as err:
        msg = err.message
        logging.error('unable to handle new post :: {}'.format(msg))
        resp_data['text'] = msg
    finally:
        resp = Response(content_type='application/json')
        resp.set_data(json.dumps(resp_data))
        return resp


def get_fact(firstname ='', lastname ='', category =''):
    """
    Fetch a Chuck Norris fact from the api.
    """
    try:
        # Prepare params to pass to the api
        params = {}
        if bool(firstname) and bool(firstname.strip()):
            params['firstName'] = firstname
        if bool(lastname) and bool(lastname.strip()):
            params['lastName'] = lastname
        if bool(category) and bool(category.strip()):
            params['category'] = [category]

        resp = requests.get('{}://api.icndb.com/jokes/random'.format(SCHEME), params=params, verify=True)

        if resp.status_code is not requests.codes.ok:
            logging.error('Encountered error using Chuck Norris API, firstname="%s", lastname="%s", status=%d, response_body=%s' % (firstname, lastname, resp.status_code, resp.json()))
            return None

        resp_data = resp.json()

        return resp_data['value']['joke']
    except Exception as err:
        logging.error('unable to fetch Chuck Norris fact :: {}'.format(err))
        return None
