#!/usr/bin/env python3
"""Word count mapper."""
import sys
import logging

logging.basicConfig(level=logging.DEBUG)

for line in sys.stdin:
	document = line.partition("\t")
	document = [*document[0].split(','), document[2].strip()]
	key = document[0]
	print(f"{key}\t{','.join(document[1:])}")
