#!/usr/bin/env python3
"""
Template reducer.

https://github.com/eecs485staff/madoop/blob/main/README_Hadoop_Streaming.md
"""
import sys
import itertools


def reduce_one_group(key, group):
	"""Reduce one group."""
	count = 0
	out = ""
	for item in group:
		val = item.partition("\t")
		arr = val[0].split(",")
		id = arr[1]
		term_freq = arr[2]
		count += int(val[2])
		out += id + "," + term_freq + ","
	print(f'{key}\t{count},{out[:-1]}')


def keyfunc(line):
    """Return the key from a TAB-delimited key-value pair."""
    return line.partition("\t")[0].split(",")[0]


def main():
    """Divide sorted lines into groups that share a key."""
    for key, group in itertools.groupby(sys.stdin, keyfunc):
        reduce_one_group(key, group)


if __name__ == "__main__":
    main()