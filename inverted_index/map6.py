#!/usr/bin/env python3
"""Word count mapper."""
import sys

for line in sys.stdin:
	document = line.strip().partition('\t')
	word = document[0]
	doc_id = document[2].split(',')[1]
	print(f'{doc_id}\t{word},{document[2].strip()}')
