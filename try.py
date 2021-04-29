#!/usr/bin/env python3

#usage: python3 exam4.py -read ATTTGGATT -k 3

import pandas as pd

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-read')
parser.add_argument('-k')
args = parser.parse_args()

#read = input("Enter read: ")
#print(read)
#k= int(input("Enter k: "))

read = args.read
k = int(args.k)


#### question 1 ####
# function to count kmers of size k
def count_kmers_observed(read, k):
    counts = {}
    num_kmers = len(read) - k + 1
    for i in range (num_kmers):
        kmer= read[i:i+k]
        if kmer not in counts:
            counts[kmer] = 0
        counts[kmer] +=1
    return counts

#print(len(count_kmers_observed(read, k)))

#### question 2 ####
# function to count possible kmers
#num_kmers = []
def count_kmers_possible(read, k):
  num_kmers = {}
  num_kmers1 = len(read) - k + 1
  num_kmers2 = 4**k
#num_kmers.append(min(num_kmers1,num_kmers2))
  num_kmers = min(num_kmers1,num_kmers2)
  return(num_kmers)
#print(len(count_kmers_observed(read,k)))



## function to create pandas df of possible and observed kmers ##
#get first column
def create_panda(read):
  k_values = []
  for i in range(1,len(read)+1):
    k_values.append(i)
  observed_kmers = []
  for i in k_values:
    observed_kmers.append(len(count_kmers_observed(read, i)))
  possible_kmers = []
  for i in k_values:
    possible_kmers.append(count_kmers_possible(read, i))
  df = pd.DataFrame(list(zip(k_values, observed_kmers, possible_kmers)), columns = ['k','observed kmers','possible kmers'])
  df.at['Total', 'observed kmers'] = df['observed kmers'].sum()
  df.at['Total', 'possible kmers'] = df['possible kmers'].sum()
  return(df)

### Question 3 ###
#function to calculate total linguistic complexity (total observed/ total possible)
def calculate_LC(read):
  k_values = []
  for i in range(1,len(read)+1):
    k_values.append(i)
  observed_kmers = []
  for i in k_values:
    observed_kmers.append(len(count_kmers_observed(read, i)))
  possible_kmers = []
  for i in k_values:
    possible_kmers.append(count_kmers_possible(read, i))
  df = pd.DataFrame(list(zip(k_values, observed_kmers, possible_kmers)), columns = ['k','observed kmers','possible kmers'])
  df.at['Total', 'observed kmers'] = df['observed kmers'].sum()
  df.at['Total', 'possible kmers'] = df['possible kmers'].sum()
  x = int(df.at['Total', 'observed kmers'])
  y = int(df.at['Total', 'possible kmers'])
  LC = (x/y)
  return(LC)
#calculate_LC('ATTTGGATT')

def main():
  fn = open("falco.txt","r+")
  for i, line in enumerate(fn):
    f = open("falco_%i.txt" %i,'w+')
    panda = create_panda(line)
    LingC = calculate_LC(line)
    f.write(line)
    f.write(str(LingC))
    f.close()
    panda.to_csv('data%i.csv' %i)
    
main()
  
