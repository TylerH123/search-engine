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
