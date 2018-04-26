def find_triple(n):
  for c in range(n):
      for b in range(c):
        for a in range (b):
          if a ** 2 + b ** 2 == c ** 2 and a + b + c == n:
            return a * b * c
print(find_triple(1000))