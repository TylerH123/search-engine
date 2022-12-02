#!/usr/bin/env python3
"""
Template reducer.

https://github.com/eecs485staff/madoop/blob/main/README_Hadoop_Streaming.md
"""
import sys
import itertools
import math


def reduce_one_group(key, group):
	"""Reduce one group."""
	for item in group:
		val = item.strip().partition("\t")
		arr = val[2].split(",")

		summation = 0
		for i in range(1, len(arr), 3):
			summation += float(arr[i])

		idf = arr[0]
		for i in range(1, len(arr), 3):
			out = ','.join(arr[i:i+2])
			print(f'{val[0]}\t{out},{summation}')



def keyfunc(line):
		"""Return the key from a TAB-delimited key-value pair."""
		return line.partition("\t")[0]


def main():
	"""Divide sorted lines into groups that share a key."""
	for key, group in itertools.groupby(sys.stdin, keyfunc):
		reduce_one_group(key, group)


if __name__ == "__main__":
		main()