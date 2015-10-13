#!/usr/bin/env python

# Command line script to calculate base frequency from a .fasta file

import sys
import argparse


parser= argparse.ArgumentParser()
parser.add_argument("DNA")
args = parser.parse_args()


a_count = 0
c_count = 0
g_count = 0
t_count = 0

with open(args.DNA, 'r') as fasta:
    for line in fasta:
        if line.startswith(">"):
            # Header line, skip it
            continue
        for base in line.strip():
            if base == "A":
                a_count += 1
            elif base == "C":
                c_count += 1
            elif base == "G":
                g_count += 1
            elif base == "T":
                t_count += 1

print("Base counts for file %s:" % args.DNA)
print("A: %d" % a_count)
print("C: %d" % c_count)
print("G: %d" % g_count)
print("T: %d" % t_count)
