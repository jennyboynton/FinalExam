#!/usr/bin/env python3

import argparse

def count_kmers_observed(read, k):
  counts = {}
  num_kmers = len(read) - k + 1
  for i in range (num_kmers):
    kmer= read[i:i+k]
    if kmer not in counts:
        counts[kmer] = 0
    counts[kmer] +=1
  return counts

def count_poss(read, k):
  counts = {}
num_kmers1 = len(read) - k + 1
num_kmers2 = 4**k
num_kmers = min(num_kmers1,num_kmers2)
print(num_kmers)


def main(args):
  assert args.k >=0
  poss = count_poss(args.read, args.k)
  observed = count_kmers_observed(args.read, args.k)
  return(poss, observed)

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('read', type = str)
  parser.add_argument('k', type = int)
  args = parser.parse_args()
  main(args)
