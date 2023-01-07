"""Importing both lower and upper case alphabet"""
import string
alphabet = list(string.ascii_lowercase) + list(string.ascii_uppercase)          

"""Loading data from the text file"""
with open('input.txt') as f:
    lines = f.readlines()

"""List of rucksacks"""
rucksacks = []
for item in lines:
    new_item = item.strip()
    rucksacks.append(new_item)

"""Dividing the elves by groups of three"""
group_list = []
start = 0
end = len(rucksacks)
step = 3
for i in range(start, end, step):
    x = i
    group_list.append(rucksacks[x:x+step])

"""Finding the item type that corresponds to the badges of each three-Elf group and converting it into priority"""
priorities = []
for i in range(len(group_list)):
    for j in range(len(group_list[i][0])):
        if group_list[i][0][j] in group_list[i][1] and group_list[i][0][j] in group_list[i][2]:
            index = alphabet.index(group_list[i][0][j])
            priorities.append(index+1)
            break

"""Calculating the sum of priorities"""
sum = 0

for priority in priorities:
    sum += priority
print(sum)                  # result for the part 2
