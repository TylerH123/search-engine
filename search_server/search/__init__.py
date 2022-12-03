import flask

app = flask.Flask(__name__)

import search.views

app.config.from_object('search.config')

# flask --app search run --host 0.0.0.0 --port 8000
# export FLASK_DEBUG=1
