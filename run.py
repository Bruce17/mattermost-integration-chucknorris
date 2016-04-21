#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

from mattermost_chucknorris.app import app
from mattermost_chucknorris.settings import *


if __name__ == "__main__":
    port = os.environ.get('MATTERMOST_GIPHY_PORT', None) or os.environ.get('PORT', 5000)
    host = os.environ.get('MATTERMOST_GIPHY_HOST', None) or os.environ.get('HOST', '127.0.0.1')
    app.run(host=str(host), port=int(port))