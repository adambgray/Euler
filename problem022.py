import string


thisfile = open("p022_names.txt", "r")
namestring = thisfile.read()
namestring = namestring.replace('"', '')
name_list = namestring.split(",")
name_list = sorted(name_list, key=str.upper)

total_namescore = 0

def calculate_namescore(name):
    namescore = 0
    for c in name:
        namescore += (string.ascii_uppercase.find(c) + 1)
    namescore *= (name_list.index(name) + 1)
    return namescore

def sum_namescore(alist):
    total_namescore = 0
    for name in alist:
        total_namescore += calculate_namescore(name)
    return total_namescore

print(sum_namescore(name_list))





