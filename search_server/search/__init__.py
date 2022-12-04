import flask
import os

app = flask.Flask(__name__)
app.config.from_object('search.config')

import search.views
import search.model

# flask --app search --debug run --host 0.0.0.0 --port 8000
# export FLASK_DEBUG=1