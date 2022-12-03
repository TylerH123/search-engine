import flask
import os

app = flask.Flask(__name__)

import index.api

inverted_index = {}
pagerank = {}
app.config['INDEX_PATH'] = os.getenv('INDEX_PATH', 'inverted_index_1.txt')
index.api.load_index(inverted_index, pagerank)



# Command to run flask app:
# flask --app index --debug run --host 0.0.0.0 --port 9000