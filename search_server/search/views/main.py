import flask
import search
import requests
import threading


def send_query(query):
    """Create threads to send requests with query to servers."""
    threads = []
    api_urls = search.app.config.get('SEARCH_INDEX_SEGMENT_API_URLS')

    for server in api_urls:
        thread = threading.Thread(
            target=request_to_server, args=(server, query))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()


def request_to_server(server, query):
    try:
      request = requests.get(server, params=query)
      print(request)
    except:
      print('reached')
      return


@search.app.route('/')
def show_index():
    """Show index."""

    query_phrase = flask.request.args.get('q')
    pagerank_weight = flask.request.args.get('w')

    if query_phrase:
        query = {
            query_phrase: query_phrase,
            pagerank_weight: pagerank_weight
        }
        send_query(query)

    context = {}
    return flask.render_template('index.html', **context)
