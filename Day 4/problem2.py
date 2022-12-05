import interval

file = open("input1.txt")
lines = file.readlines()
file.close()

def does_overlap(elf1, elf2):
    x = min(elf1[1], elf2[1]) - max(elf1[0], elf2[0])
    return x >= 0

overlaps = 0

for line in lines:
    info = (line[0:len(line)-1].split(','))
    elf1_range = info[0].split('-')
    elf2_range = info[1].split('-')
    
    is_overlapping = does_overlap([eval(i) for i in elf1_range], [eval(i) for i in elf2_range])
    if is_overlapping:
        overlaps += 1

print(overlaps)