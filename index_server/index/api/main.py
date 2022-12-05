"""Flask app routes for index server API."""
import os
import re
from math import sqrt
import collections
import flask
import index


def load_index(inverted_index, pagerank):
    """Load index into memory."""
    index_path = index.app.config['INDEX_PATH']
    index_path = os.getcwd()+"/index_server/index/inverted_index/"+index_path
    with open(index_path, "r", encoding='utf-8') as file:
        for line in file:
            line = line.split(" ")
            inverted_index[line[0]] = (" ".join(line[1:])).strip()
    pagerank_path = os.getcwd() + "/index_server/index/pagerank.out"
    with open(pagerank_path, "r", encoding='utf-8') as file:
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
    weight = float(flask.request.args.get('w', 0.5))
    hits = []
    query_terms_list = clean_query(query)
    for term in query_terms_list:
        if term not in index.inverted_index:
            context = {
                'hits': hits
            }
            return flask.jsonify(**context), 200
    process_query(query_terms_list, hits, weight)
    hits.sort(key=lambda x: x['score'], reverse=True)
    context = {
        'hits': hits
    }
    return flask.jsonify(**context), 200


def remove_stop_words(word):
    """Remove stop words."""
    return word not in index.stop_words


def clean_query(query):
    """Clean query."""
    text = re.sub(r"[^a-zA-Z0-9 ]+", "", query).casefold()
    terms = text.split()
    filtered_terms = list(filter(remove_stop_words, terms))
    return filtered_terms


def process_query(query, hits, weight):
    """Process query."""
    idf = {}
    query_freq = collections.defaultdict(int)
    term_freq = {}
    norm_fac = {}
    terms = []
    for word in query:
        if word not in query_freq:
            terms.append(word)
        query_freq[word] += 1
    result_set = get_resulting_docs(terms, idf, term_freq, norm_fac)
    query_vec = get_query_vector(query_freq, idf, terms)
    norm_q = get_norm(query_vec)
    for doc_id in result_set:
        doc_vec = get_doc_vector(idf, terms, term_freq, doc_id)
        tfidf = dot(query_vec, doc_vec) / (norm_q * sqrt(norm_fac[doc_id]))
        hits.append({
            'docid': doc_id,
            'score': weight * index.pagerank[doc_id] + (1 - weight) * tfidf
        })


def get_resulting_docs(terms, idf, term_freq, norm_fact):
    """Get resulting docs."""
    result_set = []
    for word in terms:
        result = set()
        docs = index.inverted_index[word]
        docs = docs.split(" ")
        idf[word] = float(docs[0])
        i = 1
        documents = {}
        while i < len(docs):
            doc_id = int(docs[i])
            result.add(doc_id)
            documents[doc_id] = int(docs[i+1])
            if doc_id not in norm_fact:
                norm_fact[doc_id] = float(docs[i+2])
            i += 3
        term_freq[word] = documents
        result_set.append(result)
    result_docs = result_set[0]
    for result in result_set:
        result_docs = result.intersection(result_docs)
    return result_docs


def get_query_vector(freq, idf, terms):
    """Get query vector."""
    query_vec = []
    for word in terms:
        result = freq[word] * idf[word]
        query_vec.append(result)
    return query_vec


def get_doc_vector(idf, terms, term_freq, doc_id):
    """Get doc vector."""
    doc_vec = []
    for word in terms:
        result = term_freq[word][doc_id] * idf[word]
        doc_vec.append(result)
    return doc_vec


def dot(vec1, vec2):
    """Calculate dot product."""
    result = 0
    for (ele1, ele2) in zip(vec1, vec2):
        result += ele1 * ele2
    return result


def get_norm(vec):
    """Calculate normalization."""
    result = 0
    for val in vec:
        result += val ** 2
    return sqrt(result)
