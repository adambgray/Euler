def square_sum(n):
  x = 0
  for i in range(n + 1):
    x += i
  return (x ** 2)
  
def sum_square(n):
  x = 0
  for i in range(n + 1):
    x += (i ** 2)
  return x

print (square_sum(100) - sum_square(100))  