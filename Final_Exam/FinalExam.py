#!/usr/bin/env python3

#usage: python3 exam4.py -read ATTTGGATT -k 3

import pandas as pd
import argparse


#### question 1 ####
# function to count observed kmers of size k
def count_kmers_observed(read, k):
  """Generate a count of the number of observed kmers for a string.
  
  This is a function for counting observed kmers generally used for a sequence of DNA and should only include the letters "A","T","C","G"
  
  Parameters:
  Read(str): A string of the letters "A","T","C","G" of any length
  k(int): The kmers you are looking to observe from the sequence
  
  Returns:
  A count of how many times the length kmers appears uniquely in the inputted sequence
  """
  counts = {}
  num_kmers = len(read) - k + 1
  for i in range (num_kmers):
      kmer= read[i:i+k]
      if kmer not in counts:
          counts[kmer] = 0
      counts[kmer] +=1
  return len(counts)

#print(len(count_kmers_observed(read, k)))

#### question 2 ####
# function to count possible kmers
#num_kmers = []
def count_kmers_possible(read, k):
  """Generate a count of the number of possible kmers for a string.
  
  This is a function for counting possible kmers generally used for a sequence of DNA and should only include the letters "A","T","C","G"
  
  Parameters:
  Read(str): A string of the letters "A","T","C","G" of any length
  k(int): The kmers you are looking to observe from the sequence
  
  Returns:
  A count of how many times the length kmers can possibly appear uniquely in the inputted sequence
  """
  num_kmers = {}
  num_kmers1 = len(read) - k + 1
  num_kmers2 = 4**k
#num_kmers.append(min(num_kmers1,num_kmers2))
  num_kmers = min(num_kmers1,num_kmers2)
  num_kmers3 = max(num_kmers,0)
  return(num_kmers3)
#print(len(count_kmers_observed(read,k)))



## function to create pandas df of possible and observed kmers ##
#get first column
def create_panda(read):
  """Generate a pandas data frame for each observed and possible kmers for a string.
  
  This is a function for creating a pandas data frame including counts of both observed and possible kmers for all possible kmer lengths for a sequence. 
  
  Parameters:
  Read(str): A string of the letters "A","T","C","G" of any length
  
  Returns:
  A pandas data frame with columns for k, possible kmers, and observed kmers. Possible kmers and observed kmers should produce a row at the bottom with their total sum.
  """
  k_values = []
  for i in range(1,len(read)+1):
    k_values.append(i)
  observed_kmers = []
  for i in k_values:
    observed_kmers.append((count_kmers_observed(read, i)))
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
  """Generate the linguistic complexity for a string.
  
  This is a function for calculating the linguistic complexity of a sequence; it uses the total possible kmers and divides that by total obsered kmers to generate a decimal that should be less than or equal to 1.
  
  Parameters:
  Read(str): A string of the letters "A","T","C","G" of any length
  
  Returns:
  A decimal less than or equal to one
  """
  k_values = []
  for i in range(1,len(read)+1):
    k_values.append(i)
  observed_kmers = []
  for i in k_values:
    observed_kmers.append((count_kmers_observed(read, i)))
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

#function created to ensure the string being inputted contains the proper letters
def letter_check(read):
  """Checks to make sure sequence only contains A,C,T or G
  
  This is a function for checking that any inputted sequence only contains A,C,T or G
  
  Parameters:
  Read(str): A sequence of the letters "A","T","C", and "G" in any length and order
  
  Returns:
  0 if the sequence contains any letters other than A, C, T or G 
  OR 1 if the sequence only contains the correct letters
  """
  string="ACTG"
  for line_number,line in enumerate(read):
          sequence=line.rstrip()
          if any(x not in string for x in sequence):
              return 0
  return 1
  

### Question 5 ###
#main function to read in file and output results to files
def main(args):
  """Creates new output files for both linguistic complexity and pandas data frame.
  
  This is a function for generating new file sets for each sequence in a input file. The new file sets are renamed and contain linguistic complexity values in the first set, and pandas data frames in the second set.
  
  Parameters:
  Args(str): A filename of a file containing one or more sequences of the letters "A","T","C", and "G"
  
  Returns:
  2 New files for each sequence; one containing the sequence and a linguistic complexity decimal and the second containing a pandas data frame for the sequence. The first should be named after the original file and 
  numbered(originalfile_#.txt) and the second should be named "string_examples_#.txt" with the number matching that of the first file.
  Note: If any of the sequences in a file contain letters other than A,C,T, or G the function will output: 'Sequence XXX includes letters other than A,C,T or G, please revise this sequence'
  """
  fn = open(args.filename,"r+")
  for i, line in enumerate(fn, start = 1):
    f = open("string_examples_%i.txt" %i,'w+')
    check = letter_check(line.rstrip())
    if check == 0:
      print('Sequence:', line.rstrip(), ' includes letters other than A,C,T or G, please revise this sequence')
    else:
      panda = create_panda(line.rstrip())
      LingC = calculate_LC(line.rstrip())
      f.write(line)
      f.write(str(LingC))
      f.close()
      panda.to_csv('data%i.csv' %i)
    

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('filename', type = str)
  args = parser.parse_args()
  main(args)  



