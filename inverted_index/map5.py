#!/usr/bin/env python3
"""Word count mapper."""
import sys

for line in sys.stdin:
	doc = line.strip().partition("\t")
	key = doc[0]
	val = doc[2].split(",")
	term = val[0]
	body = val[2] + " " + key + " " + val[1] + " " + val[3]
	print(f"{int(key) % 3}\t{term} {body}")