# Chuck Norris facts Integration Service for Mattermost

## Requirements

* Python v2.7

Install application requirements e.g. via `python -m pip install -r requirements.txt`.
Heroku will automatically install requirements in your `requirements.txt` file automatically.


## Install

### Heroku-based install

Please visit the steps at [mattermost-integration-giphy#heroku-based-install](https://github.com/numberly/mattermost-integration-giphy#heroku-based-install).

#### Return new fact

4.ii.
    Please change your slash command's name e.g. to `/cn`.

4.vi.
    (optional) Check the autocomplete checkbox, add `[FIRSTNAME] [LASTNAME] [CATEGORY]` as the hint, `Returns a Chuck Norris fact from the Chuck Norris API on the keyword. Post without any parameters to get a random fact with default settings.` as the description and `Get a fact from the Chuck Norris API` as the descriptive label

#### Return a random fact

4.ii.
    Please change your slash command's name e.g. to `/cn-random`.

4.vi.
    (optional) Check the autocomplete checkbox, add `` as the hint, `Returns a random Chuck Norris fact from the Chuck Norris API on the keyword` as the description and `Get a random fact from the Chuck Norris API` as the descriptive label


## Startup

### Heroku

Heroku will start the machine using the given `Procfile`.

### Local development

#### Windows

Use the command `SET DEBUG=True&& python run.py` to start the server in development mode. It will auto restart on file changes.

#### Linux

Command: `export DEBUG=True&& python run.py`

### Normal startup

Just call `python run.py` to start the service.
