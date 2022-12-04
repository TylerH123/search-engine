#!/usr/bin/env python3
"""
Template reducer.

https://github.com/eecs485staff/madoop/blob/main/README_Hadoop_Streaming.md
"""
import sys
import itertools
import collections


def reduce_one_group(key, group):
    """Reduce one group."""
    term_docs = {}
    # print("---------------------------------------")
    for line in group:
        # print(line.strip().partition("\t")[2].split(" "))
        doc = line.strip().partition("\t")[2].split(" ")
        term = doc[0]
        if term in term_docs:
            term_docs[term] += " " + " ".join(doc[2:])
        else:
            term_docs[term] = " ".join(doc[1:])
    for k,val in term_docs.items(): 
        print(f"{k} {val}")


def keyfunc(line):
    """Return the key from a TAB-delimited key-value pair."""
    return line.partition("\t")[0]


def main():
	"""Divide sorted lines into groups that share a key."""
	for key, group in itertools.groupby(sys.stdin, keyfunc):
		reduce_one_group(key, group)


if __name__ == "__main__":
    main()