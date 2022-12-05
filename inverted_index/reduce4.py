#!/usr/bin/env python3
"""Inverted index reducer."""
import sys
import itertools


def reduce_one_group(key, group):
    """Reduce one group."""
    vals = []
    norm_fac = 0
    for item in group:
        val = item.strip().partition("\t")[2]
        vals.append(val)
        tf_idf = float(val.split(",")[-1])
        norm_fac += tf_idf
    for val in vals:
        arr = val.split(",")
        arr[-1] = str(norm_fac)
        out = ",".join(arr)
        print(f'{key}\t{out}')


def keyfunc(line):
    """Return the key from a TAB-delimited key-value pair."""
    return line.partition("\t")[0]


def main():
    """Divide sorted lines into groups that share a key."""
    for key, group in itertools.groupby(sys.stdin, keyfunc):
        reduce_one_group(key, group)


if __name__ == "__main__":
    main()
