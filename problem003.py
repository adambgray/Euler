def is_prime(n):
  """determines if an integer is prime"""
  if n < 2:
    return False
  if n == 2 or n == 3:
    return True
  elif n % 2 == 0:
      return False
  else:
    x = 0
    for i in range(3, n, 2):
      if n % i == 0:
        x = 1
    return x == 0

def list_primes(n):
  """Generates a list of primes < n starting with 2"""
  primeList = []
  for i in range(n):
    if is_prime(i):
      primeList.append(i)
  return primeList

def find_factors(number):
    factor_list = []
    for n in range(3, number, 2):
        if number % n == 0:
            if is_prime(n):
                print(n)

find_factors(600851475143)
