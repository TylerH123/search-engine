#!/usr/bin/env python3
"""
Template reducer.

https://github.com/eecs485staff/madoop/blob/main/README_Hadoop_Streaming.md
"""
import sys
import itertools
import math


def get_total_documents(): 
	with open("total_document_count.txt", "r") as file:
		return int(file.readline().strip())


def reduce_one_group(key, group):
	"""Reduce one group."""
	num_docs = get_total_documents()
	count = 0
	doc_ids = {}
	# key to this group is the term
	for item in group:
		val = item.strip().partition("\t")[2].split(",")
		id = int(val[0]) 
		freq = int(val[2])
		doc_ids[id] = [key, freq]
		count += 1
	for k, val in doc_ids.items(): 
		idf = math.log(num_docs / count, 10)
		if idf <= 0: 
			idf = 0.0
		tf_idf = (val[1] * idf) ** 2
		print(f"{k}\t{key},{val[1]},{idf},{tf_idf}")


def keyfunc(line):
	"""Return the key from a TAB-delimited key-value pair."""
	return line.partition("\t")[0]


def main():
	"""Divide sorted lines into groups that share a key."""
	for key, group in itertools.groupby(sys.stdin, keyfunc):
		reduce_one_group(key, group)


if __name__ == "__main__":
		main()