with open("p011_matrix.txt", "r") as ins:
    array = []
    for line in ins:
        array.append(line.rstrip('\n').split(' '))

for i in range(20):
    for j in range(20):
        array[i][j] = int(array[i][j])

highest_product = 0

for i in range(20):
    for j in range(17):
        product = array[i][j] * array[i][j+1] * array[i][j+2] * array[i][j+3]
        if product > highest_product:
            highest_product = product

for i in range(17):
    for j in range(17):
        product = array[i][j] * array[i+1][j+1] * array[i+2][j+2] * array[i+3][j+3]
        if product > highest_product:
             highest_product = product

for i in range(3, 20):
    for j in range(17):
        product = array[i][j] * array[i-1][j+1] * array[i-2][j+2] * array[i-3][j+3]
        if product > highest_product:
            highest_product = product

for i in range(17):
    for j in range(20):
        product = array[i][j] * array[i+1][j] * array[i+2][j] * array[i+3][j]
        if product > highest_product:
            highest_product = product
    
print(highest_product)

