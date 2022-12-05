#!/usr/bin/env python3
"""Inverted index reducer."""
import sys
import itertools


def reduce_one_group(key, group):
    """Reduce one group."""
    assert key
    document_count = 0
    for item in group:
        document_count += int(item.partition("\t")[2])
    print(f'{document_count}')


def keyfunc(line):
    """Return the key from a TAB-delimited key-value pair."""
    return line.partition("\t")[0]


def main():
    """Divide sorted lines into groups that share a key."""
    for key, group in itertools.groupby(sys.stdin, keyfunc):
        reduce_one_group(key, group)


if __name__ == "__main__":
    main()
