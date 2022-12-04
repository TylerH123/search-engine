import flask
import os
import search
import requests
import threading


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
        # response = requests.get(
        #     'http://localhost:9000/api/v1/', params=query).json()
    #   hits = response.get('hits')
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
        print(hits)

    except:
        print('reached')
        return