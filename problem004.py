def generate_product_list():
  productList = []
  for i in range(100,1000):
    for d in range(100,1000):
      productList.append(int(i * d))
  return productList


def if_palindrome():
  palindromeList = []
  for product in generate_product_list():
    if len(str(product)) == 6 and (str(product)[0]) == (str(product)[5]) and (str(product)[1]) == (str(product)[4]) and (str(product)[2]) == (str(product)[3]):
      palindromeList.append(product)
  return palindromeList
    
      
print(max(if_palindrome()))