with open('input.txt') as f:
    lines = f.readlines()

new_list = []

# Converting values into integers
for i in range(len(lines)):
        try:
            new_item = int(lines[i])
        except ValueError:
            new_item = "prazdno"
        new_list.append(new_item)

# creating sublist for each elf
big_list = []
small_list = []

for item in new_list:
    if item != "prazdno":
        small_list.append(item)
        if (new_list.index(item) + 1) == len(new_list):
            big_list.append(small_list)
    elif item == "prazdno":
        big_list.append(small_list)
        small_list = []
    if (new_list.index(item) + 1) == len(new_list):
        big_list.append(small_list)
# print(big_list) - control print

# Creating new list made of total calories per elf
total_calories_per_elf = []
total = 0

for i in range(len(big_list)):
    for j in range(len(big_list[i])):
        total += big_list[i][j]
    total_calories_per_elf.append(total)
    total = 0

print(max(total_calories_per_elf))              # part 1 result

top_three = 0
top_three += max(total_calories_per_elf)        # the first elf carrying the most calories
 
total_calories_per_elf.remove(max(total_calories_per_elf))

top_three += max(total_calories_per_elf)        # the second elf carrying the most calories
total_calories_per_elf.remove(max(total_calories_per_elf))

top_three += max(total_calories_per_elf)        # the third elf carrying the most calories

print(top_three)                                # result part 2

