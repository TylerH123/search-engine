#!/usr/bin/env python3
import sys

for line in sys.stdin:
  print("doc\t1")


# #!/usr/bin/env python3
# """Word count mapper."""
# import csv
# import os
# import re
# import sys

# # For documents with very large doc_body
# csv.field_size_limit(sys.maxsize)

# stop_words = set() 
# current_dir = os.path.dirname(__file__)
# with open(os.path.join(current_dir ,'stopwords.txt'), 'r') as f:
#   for word in f.read().splitlines():
#     stop_words.add(word)


# def remove_stop_words(word):
#   return word not in stop_words


# for line in sys.stdin:
#   document = line.split(',')
#   doc_id = int(document[0][1:-1])

#   # Join doc_title and doc_body and strip remove all non-alphanumerics
#   joined_title_body = ' '.join(document[1:])
#   text = re.sub(r"[^a-zA-Z0-9 ]+", "", joined_title_body).casefold()

#   # Remove all stop words
#   terms = text.split()
#   filtered_terms = list(filter(remove_stop_words, terms))
  
#   print(doc_id)
#   print(filtered_terms)