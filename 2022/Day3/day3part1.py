"""Importing both lower and upper case alphabet"""
import string
alphabet = list(string.ascii_lowercase) + list(string.ascii_uppercase)          

"""Loading data from the text file"""
with open('input.txt') as f:
    lines = f.readlines()

"""Splitting each string in half creating two rucksack compartments"""
rucksacks = []

for item in lines:
    new_item = item.strip()
    firstcompartment, secondcompartment = new_item[:len(new_item)//2], new_item[len(new_item)//2:]
    rucksacks.append([firstcompartment, secondcompartment])

"""Finding the item that appears in both compartments and converting it into its priority"""
priorities = []

for i in range(len(rucksacks)):
    for j in range(len(rucksacks[i][0])):
        if rucksacks[i][0][j] in rucksacks[i][1]:
            index = alphabet.index(rucksacks[i][0][j])
            priorities.append(index+1)
            break

"""Calculating the sum of priorities"""
sum = 0

for priority in priorities:
    sum += priority
print(sum)                          # result for the part 1
