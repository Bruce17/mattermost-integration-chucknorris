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

@app.route('/random')
def random():
    """
    Get a random Chuck Norris fact
    """

    try:
        resp_data = {}
        resp_data['username'] = USERNAME
        resp_data['icon_url'] = ICON_URL

        resp_data['text'] = get_fact()
    except Exception as err:
        msg = err.message
        logging.error('unable to handle new post :: {}'.format(msg))
        resp_data['text'] = msg
    finally:
        resp = Response(content_type='application/json')
        resp.set_data(json.dumps(resp_data))
        return resp

# @app.route('/new_fact', methods=['POST'])
# def new_fact():
#     """
#     Get a Chuck Norris fact using a "firstname" & "lastname"
#     """
#     try:
#         # NOTE: common stuff
#         slash_command = False
#         resp_data = {}
#         resp_data['username'] = USERNAME
#         resp_data['icon_url'] = ICON_URL
#
#         data = request.form
#
#         # TODO: implement me
#     except Exception as err:
#         msg = err.message
#         logging.error('unable to handle new post :: {}'.format(msg))
#         resp_data['text'] = msg
#     finally:
#         resp = Response(content_type='application/json')
#         resp.set_data(json.dumps(resp_data))
#         return resp


def get_fact(firstname = '', lastname = ''):
    """
    Fetch a Chuck Norris fact from the api.
    """
    try:
        params = {}
        if bool(firstname) and bool(firstname.strip()):
            params['firstName'] = firstname
        if bool(lastname) and bool(lastname.strip()):
            params['lastName'] = lastname

        resp = requests.get('{}://api.icndb.com/jokes/random'.format(SCHEME), params=params, verify=True)

        if resp.status_code is not requests.codes.ok:
            logging.error('Encountered error using Chuck Norris API, firstname="%s", lastname="%s", status=%d, response_body=%s' % (firstname, lastname, resp.status_code, resp.json()))
            return None

        resp_data = resp.json()

        return resp_data['value']['joke']
    except Exception as err:
        logging.error('unable to fetch Chuck Norris fact :: {}'.format(err))
        return None
