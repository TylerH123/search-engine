#!/usr/bin/env python3
"""
Template reducer.

https://github.com/eecs485staff/madoop/blob/main/README_Hadoop_Streaming.md
"""
import sys
import itertools
import math
import logging


def reduce_one_group(key, group):
	"""Reduce one group."""
	for item in group:
		print(item.strip())
		


def keyfunc(line):
		"""Return the key from a TAB-delimited key-value pair."""
		logging.debug(line.split()[2])
		return line.split()[2]


def main():
	"""Divide sorted lines into groups that share a key."""
	for key, group in itertools.groupby(sys.stdin, keyfunc):
		reduce_one_group(key, group)


if __name__ == "__main__":
		main()