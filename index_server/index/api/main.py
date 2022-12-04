import collections
import flask
import index
import os
import re
from math import sqrt

def load_index(inverted_index, pagerank):
  index_path = index.app.config['INDEX_PATH']
  index_path = os.getcwd() + "/index_server/index/inverted_index/" + index_path
  with open(index_path, "r") as file:
    for line in file:
      line = line.split(" ")
      inverted_index[line[0]] = (" ".join(line[1:])).strip()
  pagerank_path = os.getcwd() + "/index_server/index/pagerank.out"
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
  hits = []
  query_terms_list = clean_query(query)
  process_query(query_terms_list, hits, weight)
  hits.sort(key=lambda x: x['score'], reverse=True)
  context = {
    'hits': hits
  }
  return flask.jsonify(**context), 200


def remove_stop_words(word):
  return word not in index.stop_words


def clean_query(query):
  text = re.sub(r"[^a-zA-Z0-9 ]+", "", query).casefold()
  terms = text.split()
  filtered_terms = list(filter(remove_stop_words, terms))
  return filtered_terms


def process_query(query, hits, weight):
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
    dot_prod = dot(query_vec, doc_vec)
    norm_d = sqrt(norm_fac[doc_id])
    tfidf = dot_prod / (norm_q * norm_d)
    score = weight * index.pagerank[868657] \
            + (1 - weight) * (tfidf)
    out = {}
    out["docid"] = doc_id
    out["score"] = score
    hits.append(out)


def get_resulting_docs(terms, idf, tf, nf):
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
      if doc_id not in nf: 
        nf[doc_id] = float(docs[i+2])
      i += 3
    tf[word] = documents
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


def get_doc_vector(idf, terms, tf, doc_id):
  doc_vec = []
  for word in terms: 
    result = tf[word][doc_id] * idf[word]
    doc_vec.append(result)
  return doc_vec


def dot(vec1, vec2):
  result = 0
  for (ele1, ele2) in zip(vec1, vec2):
    result += ele1 * ele2
  return result


def get_norm(vec): 
  result = 0
  for val in vec: 
    result += val ** 2
  return sqrt(result)
