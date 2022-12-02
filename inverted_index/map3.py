#!/usr/bin/env python3
"""Word count mapper."""
import csv
import os
import re
import sys

for line in sys.stdin:
	document = line.partition("\t")
	key = document[0] + "," + document[2].strip()
	print(f"{key}\t{1}")

#   # Join doc_title and doc_body and strip remove all non-alphanumerics
#   joined_title_body = " ".join(document[1:])
#   text = re.sub(r"[^a-zA-Z0-9 ]+", "", joined_title_body).casefold()

#   # Remove all stop words
#   terms = text.split()
#   filtered_terms = list(filter(remove_stop_words, terms))
#   doc_body = ",".join(filtered_terms)
#   print(f"{doc_id}\t{doc_body}")
  
