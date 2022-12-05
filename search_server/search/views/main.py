"""Flask routes for search server."""
import heapq
import threading
import flask
import requests

import search
import search.model


@search.app.route('/')
def show_index():
    """Show index."""
    query_phrase = flask.request.args.get('q')
    pagerank_weight = flask.request.args.get('w')

    context = {
        'phrase': query_phrase or '',
        'weight': pagerank_weight or '0.5'
    }

    if query_phrase:
        query = {
            'q': query_phrase,
            'w': pagerank_weight
        }
        results = send_query(query)
        context['results'] = results

    return flask.render_template('index.html', **context)


def send_query(query):
    """Create parallel threads to send query to different servers."""
    threads = []
    api_urls = search.app.config.get('SEARCH_INDEX_SEGMENT_API_URLS')

    combined_responses = []
    for server in api_urls:
        thread = threading.Thread(
            target=request_to_server, args=(server, query, combined_responses))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    result_docid_list = list(heapq.merge(
        *combined_responses, key=lambda x: x['score'], reverse=True))
    results = []
    for document in result_docid_list[:10]:
        docid = document['docid']
        results.append(search.model.get_document(docid))

    return results


def request_to_server(server, query, combined_responses):
    """Send request with query to server and process response."""
    response = requests.get(server, params=query, timeout=10).json()
    hits = response.get('hits')
    combined_responses.append(hits)
