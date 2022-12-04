#!/usr/bin/env python3
"""Word count mapper."""
import sys


for line in sys.stdin:
	document = line.partition("\t")
	doc_id = int(document[0])
	text = document[2].split(",")
	for term in text: 
		print(f"{doc_id},{term.strip()}\t{1}")
