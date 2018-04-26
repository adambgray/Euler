import math

def find_lowest_common_multiple(n):

  candidatesList = range(n, math.factorial(n), n)

  for candidate in candidatesList:
    x = 0
    for d in range(1, n+1):
      if candidate % d != 0:
        x = 1 
    if x == 0:
      return candidate

        
print(find_lowest_common_multiple(20))