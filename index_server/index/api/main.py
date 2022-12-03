import flask
import index

def load_index():
  index_path = index.app.config['INDEX_PATH']
  
  return

@index.app.route('/api/v1/')
def get_api():
    """Get api routes."""
    context = {
      'hits': '/api/v1/hits/',
      'url': '/api/v1/'
    }
    return flask.jsonify(**context), 200


@index.app.route('/api/v1/hits/')
def get_hits():
  """Return hits from query."""
  query = flask.request.args.get('q')
  weight = flask.request.args.get('w') or 0.5
  context = {
    'hits': []
  }
  return flask.jsonify(**context), 200

