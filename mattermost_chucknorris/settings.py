# -*- coding: utf-8 -*-
import os

# username the bot posts as
USERNAME = os.environ.get('USERNAME', 'Chuck Norris')

# display picture the bot posts with
ICON_URL = os.environ.get('ICON_URL', 'http://rocketdock.com/images/screenshots/chuck-norris.png')

# scheme to be used for the gif url return
SCHEME = os.environ.get('SCHEME', 'http')

# the Mattemost token generated when you created your outgoing webhook
MATTERMOST_TOKEN = os.environ.get('MATTERMOST_TOKEN', None)

# Start application in debug mode e.g. to restart on file changes.
DEBUG = os.environ.get('DEBUG', False)
