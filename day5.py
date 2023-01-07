import copy
with open('stack.txt') as f:
    lines = f.readlines()

columns = list(zip(*lines))

def letters(columns):
    valids = []
    small_list = []
    for column in columns:
        for character in column:
            if character.isalpha():
                small_list.append(character)
        ''.join(small_list)
        if small_list != []:
            valids.append(small_list[::-1])
            small_list = []   
    return valids

valids = letters(columns)
with open('input.txt') as f:
    lines = f.readlines()

instructions = []
for line in lines:
    s = ''.join(x for x in line if x.isdigit())
    instructions.append(s)

small_list = []
for i in range(len(instructions)):
    if len(instructions[i]) != 3:
        a = int(instructions[i][0]+instructions[i][1])
        b = int(instructions[i][2])
        c = int(instructions[i][3])
        small_list.append([a, b, c])
    else:
        a = int(instructions[i][0])
        b = int(instructions[i][1])
        c = int(instructions[i][2])
        small_list.append([a, b, c])    

valids9000 = copy.deepcopy(valids)

def crater_mover9000(small_list,valids9000):
    for i in range(len(small_list)):
        for j in range(int(small_list[i][0])):
            a = int(small_list[i][1]) - 1               # ze kterého sloupečku budeme odebírat
            b = int(small_list[i][2]) - 1               # do kterého sloupečku budeme přídávat
            cut = valids9000[int(a)].pop()
            valids9000[int(b)].append(cut)
    return valids9000

valids9000 = crater_mover9000(small_list,valids9000)
result1 = []

for i in range(len(valids9000)):
    result1.append(valids9000[i].pop())

result_word1 = ''.join(result1)
print(result_word1)
valids9001 = copy.deepcopy(valids)

def crater_mover9001(small_list, valids9001):
    for i in range(len(small_list)):
        a = int(small_list[i][1]) - 1                   # ze kterého sloupečku budeme odebírat
        b = int(small_list[i][2]) - 1                   # do kterého sloupečku budeme přídávat
        c = int(small_list[i][0])                       # kolik krabic budeme odebírat
        cut = valids9001[int(a)][::-1][:c][::-1]
        for j in range(int(small_list[i][0])):
            valids9001[int(b)].append(cut[j])
        for k in range(int(small_list[i][0])):
            valids9001[int(a)].pop()
    return valids9001

valids9001 = crater_mover9001(small_list, valids9001)
result2 = []

for i in range(len(valids9001)):
    result2.append(valids9001[i].pop())

result_word2 = ''.join(result2)
print(result_word2)