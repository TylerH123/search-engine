#!/usr/bin/env python3
"""Word count mapper."""
import sys

for line in sys.stdin:
	doc = line.strip().partition("\t")
	key = doc[0].split(",")
	id = key[0]
	term = key[1]
	val = term + "," + doc[2]
	print(f"{id}\t{val}")