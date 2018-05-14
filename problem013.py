with open("p013_numbers.txt", "r") as ins:
    array = []
    for line in ins:
        array.append(int(line.rstrip('\n')))

total_sum = 0

for number in array:
    total_sum += number

print(str(total_sum)[:10])
