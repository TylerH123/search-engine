import collections
import flask
import index
import os
import re


def load_index(inverted_index, pagerank):
    index_path = index.app.config['INDEX_PATH']
    index_path = os.getcwd() + "/index/inverted_index/" + index_path
    with open(index_path, "r") as file:
        for line in file:
            line = line.split(" ")
            inverted_index[line[0]] = (" ".join(line[1:])).strip()
    pagerank_path = os.getcwd() + "/index/pagerank.out"
    with open(pagerank_path, "r") as file:
        for line in file:
            line = line.strip().partition(",")
            pagerank[int(line[0])] = float(line[2])


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

    query_terms_list = clean_query(query)
    process_query(query_terms_list)
    
    context = {
        'hits': []
    }
    return flask.jsonify(**context), 200


def remove_stop_words(word):
  return word not in index.stop_words


def clean_query(query):
    text = re.sub(r"[^a-zA-Z0-9 ]+", "", query).casefold()
    terms = text.split()
    filtered_terms = list(filter(remove_stop_words, terms))
    return filtered_terms


def process_query(query):
    idf = {}
    query_freq = collections.defaultdict(int)
    term_freq = {}
    terms = []
    norm_fac = {}
    for word in query:
        if word not in query_freq:
            terms.append(word)
        query_freq[word] += 1
    result_set = get_resulting_docs(terms, idf, term_freq)
    query_vec = get_query_vector(query_freq, idf, terms)
    doc_vec = get_doc_vector()


def get_resulting_docs(terms, idf, tf):
    result_set = []
    for word in terms:
        result = set()
        docs = index.inverted_index[word]
        docs = docs.split(" ")
        idf[word] = float(docs[0])
        i = 1
        while i < len(docs):
            result.add(int(docs[i]))
            i += 3
        result_set.append(result)
    result_docs = result_set[0]
    for rs in result_set:
        result_docs = rs.intersection(result_docs)
    return result_docs


def get_query_vector(freq, idf, terms):
    query_vec = []
    for word in terms:
        result = freq[word] * idf[word]
        query_vec.append(result)
    return query_vec


def get_doc_vector():
    return


# @index.app.route('/api/test/')
# def test():
#   """Return hits from query."""
#   return flask.jsonify(index.inverted_index), 200
