#!/usr/bin/env python3
"""Word count mapper."""
import sys
import logging

logging.basicConfig(level=logging.DEBUG)

for line in sys.stdin:
	doc = line.strip().partition("\t") 
	key = doc[0].split(",") 
	term = key[1]
	print(f"{term}\t{doc[0]},{doc[2]}")