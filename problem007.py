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

def list_n_primes(n):
  primeList = [2]
  x=3
  while len(primeList)< n + 1:
    if is_prime(x):
      primeList.append(x)
      x+=2
    else:
      x+=2
  return primeList    
print(list_n_primes(10001)[-1])