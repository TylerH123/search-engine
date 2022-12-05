"""Index server."""
import os
import flask


app = flask.Flask(__name__)

import index.api    # noqa: E402  pylint: disable=wrong-import-position

inverted_index = {}
pagerank = {}
app.config['INDEX_PATH'] = os.getenv('INDEX_PATH', 'inverted_index_1.txt')
index.api.load_index(inverted_index, pagerank)

stop_words = set()
current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, 'stopwords.txt')
with open(file_path, 'r', encoding='utf-8') as f:
    for word in f.read().splitlines():
        stop_words.add(word)


# Command to run flask app:
# flask --app index --debug run --host 0.0.0.0 --port 9000
