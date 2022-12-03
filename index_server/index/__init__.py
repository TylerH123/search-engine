import flask
import os

app = flask.Flask(__name__)

import index.api

app.config['INDEX_PATH'] = os.getenv('INDEX_PATH', 'inverted_index_1.txt')
index.api.load_index()

# Command to run flask app:
# flask --app index --debug run --host 0.0.0.0 --port 9000