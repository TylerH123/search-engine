import flask
import index
import os

def load_index(inverted_index):
  index_path = index.app.config['INDEX_PATH']
  index_path = os.getcwd() + "/index/inverted_index/" + index_path
  with open(index_path, "r") as file:
    for line in file:
      line = line.split(" ")
      inverted_index[line[0]] = (" ".join(line[1:])).strip()

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
  result_set = []
  query = query.split(" ")
  print(query)
  for word in query:
    docs = index.inverted_index[word]
    docs = docs.split(" ")
    print(docs)
  context = {
    'hits': []
  }
  return flask.jsonify(**context), 200

# @index.app.route('/api/test/')
# def test():
#   """Return hits from query."""
#   return flask.jsonify(index.inverted_index), 200
