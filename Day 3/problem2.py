file = open("input1.txt")
text = file.readlines()
file.close()

def find_badge(elf1, elf2, elf3):
    for c in elf1:
        if c in elf2 and c in elf3:
            return c

sum_of_priorities = 0
curr_group = []

for bag in text:
    bag = bag[0:len(bag)-1]
    curr_group.append(bag)

    if len(curr_group) == 3:
        letter = find_badge(curr_group[0], curr_group[1], curr_group[2])
        sum_of_priorities += (ord(letter)-96) if letter.islower() else (ord(letter.lower())-96+26)
        curr_group.clear()


print(sum_of_priorities)