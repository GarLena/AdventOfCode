with open('input.txt') as f:
    lines = f.readlines()

"""Creating list of sections for each pair of Elves in integers"""
new_list = []
for item in lines:
    new_item = item.strip()
    new_item = new_item.split(",")
    new_item = new_item[0].split("-") + new_item[1].split("-")
    new_item = int(new_item[0]), int(new_item[1]), int(new_item[2]), int(new_item[3])
    new_list.append(new_item)

"""Is one range a subrange of the other?"""
def is_subrange(x1,x2,y1,y2):
    if x1 <= y1 and x2 >= y2:
        return True
    elif y1 <= x1 and y2 >= x2:
        return True
    else:
        return False

"""Are ranges overlapping?"""
def overlapping(x1,x2,y1,y2):
    if y1 in range(x1,x2+1) or y2 in range(x1,x2+1):
        return True
    elif x1 in range(y1,y2+1) or x2 in range(y1,y2+1):
        return True
    else:
        return False

"""Calling both functions"""
range_included = 0
for i in range(len(new_list)):
    if is_subrange(new_list[i][0],new_list[i][1],new_list[i][2],new_list[i][3]) == True:
        range_included += 1
    
overlap = 0
for i in range(len(new_list)):
    if overlapping(new_list[i][0],new_list[i][1],new_list[i][2],new_list[i][3]) == True:
        overlap += 1

print(range_included)               # result part 1
print(overlap)                      # result part 2
