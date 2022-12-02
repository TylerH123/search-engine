#!/usr/bin/env python3
"""Word count mapper."""
import sys

for line in sys.stdin:
	items = line.split()
	w = items[1]
	for item in items[2:]:
		doc = item.split(',')
		doc[-1] = w
		out = ' '.join(doc[1:])
		print(f'{doc[0]}\t{out}')