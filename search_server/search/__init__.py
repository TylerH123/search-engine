"""Search server."""
import flask

app = flask.Flask(__name__)
app.config.from_object('search.config')

import search.views  # noqa: E402  pylint: disable=wrong-import-position
import search.model  # noqa: E402  pylint: disable=wrong-import-position

# flask --app search --debug run --host 0.0.0.0 --port 8000
# export FLASK_DEBUG=1
