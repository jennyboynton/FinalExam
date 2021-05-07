from FinalExam import *

    
def test_count_kmers_observed():
  read = 'ATTTGGATT'
  k = int(12)
  actual_result = count_kmers_observed(read, k)
  expected_result = 0
  assert actual_result == expected_result


def test_count_kmers_possible():
  read = 'ATTTGGATT'
  k = int(12)
  actual_result = count_kmers_possible(read, k)
  expected_result = 0
  assert actual_result == expected_result
  
def test_create_panda():
  read = 'ATTTGGATT'
  expected_result = pd.DataFrame(list(zip([1,2,3,4,5,6,7,8,9], [3,5,6,6,5,4,3,2,1], [4,8,7,6,5,4,3,2,1])), columns = ['k','observed kmers','possible kmers'])
  expected_result.at['Total', 'observed kmers'] = expected_result['observed kmers'].sum() 
  expected_result.at['Total', 'possible kmers'] = expected_result['possible kmers'].sum() #this is the expected table 
  
  create_panda(read).eq(expected_result) #use this pandas way (.eq) to see if the tables are the same instead of assert## for testing wrong input
  

def test_calculate_LC():
  read = 'ATTTGGATT'
  actual_result = calculate_LC(read)
  expected_result = 0.875
  assert actual_result == expected_result

def test_letter_check():
  read = 'HHU'
  actual_result = letter_check(read)
  expected_result = 0
  assert actual_result == expected_result


