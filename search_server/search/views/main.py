import flask
import heapq
import os
import search
import requests
import threading
import search.model


@search.app.route('/')
def show_index():
    """Show index."""
    query_phrase = flask.request.args.get('q')
    pagerank_weight = flask.request.args.get('w')

    context = {}

    if query_phrase:
        query = {
            query_phrase: query_phrase,
            pagerank_weight: pagerank_weight
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

    result_docid_list = list(heapq.merge(*combined_responses))

    results = []
    for docid in result_docid_list:
        results.append(search.model.get_document(docid))

    return results


def request_to_server(server, query, combined_responses):
    """Send request with query to server and process response."""
    try:
        # response = requests.get(server, params=query).json()
        # hits = response.get('hits')
        hits = [
            {
                "docid": 7279265,
                "score": 0.17852494237501587
            },
            {
                "docid": 32189768,
                "score": 0.17415374191738828
            },
        ]
        output = [item['docid'] for item in hits]
        combined_responses.append(output)

    except:
        print(f'Error when sending request to {server}')