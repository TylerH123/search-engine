#!/usr/bin/env python3
"""Word count mapper."""
import sys

for line in sys.stdin:
	document = line.partition("\t")
	doc_id = int(document[0])
	text = document[2].split(",")
	for word in text: 
		print(f"{doc_id},{word.strip()}\t{1}")
