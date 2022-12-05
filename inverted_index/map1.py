#!/usr/bin/env python3
"""Inverted index mapper."""
import csv
import os
import re
import sys


# For documents with very large doc_body
csv.field_size_limit(sys.maxsize)
stop_words = set()
current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, 'stopwords.txt')
with open(file_path, 'r', encoding='utf-8') as f:
    for term in f.read().splitlines():
        stop_words.add(term)


def remove_stop_words(word):
    """Remove stop words."""
    return word not in stop_words


for line in sys.stdin:
    document = line.split(',')
    doc_id = int(document[0][1:-1])

    # Join doc_title and doc_body and strip remove all non-alphanumerics
    JOINED_TITLE_BODY = " ".join(document[1:])
    text = re.sub(r"[^a-zA-Z0-9 ]+", "", JOINED_TITLE_BODY).casefold()

    # Remove all stop words
    terms = text.split()
    filtered_terms = list(filter(remove_stop_words, terms))
    DOC_BODY = ",".join(filtered_terms)
    print(f"{doc_id}\t{DOC_BODY}")
