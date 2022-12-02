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
		count = int(file.readline().strip())
	return count


def reduce_one_group(key, group):
	"""Reduce one group."""
	num_documents = get_total_documents()
	out = ""
	for item in group:
		val = item.partition("\t")
		arr = val[2].split(",")
		nk = int(arr[0]) 
		inverse_freq = math.log(num_documents / nk, 10)
		arr[0] = inverse_freq
		for ele in arr:
			out += str(ele).strip() + ","
	print(f'{key}\t{out[:-1]}')


def keyfunc(line):
    """Return the key from a TAB-delimited key-value pair."""
    return line.partition("\t")[0]


def main():
	"""Divide sorted lines into groups that share a key."""
	for key, group in itertools.groupby(sys.stdin, keyfunc):
		reduce_one_group(key, group)


if __name__ == "__main__":
    main()