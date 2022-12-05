#!/usr/bin/env python3
"""Inverted index mapper."""
import sys


for line in sys.stdin:
    doc = line.strip().partition("\t")
    key = doc[0].split(",")
    term = key[1]
    print(f"{term}\t{doc[0]},{doc[2]}")
