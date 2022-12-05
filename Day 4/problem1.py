file = open("input1.txt")
lines = file.readlines()
file.close()

def compare_ranges(elf1, elf2):
    return ((int(elf1[0]) <= int(elf2[0]) and int(elf1[1]) >= int(elf2[1])) or (int(elf2[0]) <= int(elf1[0]) and int(elf2[1]) >= int(elf1[1])))

contained = 0

for line in lines:
    info = (line[0:len(line)-1].split(','))
    elf1_range = info[0].split('-')
    elf2_range = info[1].split('-')
    
    is_contained = compare_ranges(elf1_range, elf2_range)
    if is_contained:
        contained += 1

print(contained)