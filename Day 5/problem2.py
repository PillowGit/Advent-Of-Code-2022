file = open('Day 5\input1.txt')
lines = file.readlines()
file.close()

crates = {
    1: ['B','L','D','T','W','C','F','M'],
    2: ['N','B','L'],
    3: ['J','C','H','T','L','V'],
    4: ['S','P','J','W'],
    5: ['Z','S','C','F','T','L','R'],
    6: ['W','D','G','B','H','N','Z'],
    7: ['F','M','S','P','V','G','C','N'],
    8: ['W','Q','R','J','F','V','C','Z'],
    9: ['R','P','M','L','H']
}

#Move crates
for line in lines:
    if 'move' in line:
        amount, move_from, move_to = [int(s) for s in line.split() if s.isdigit()]
        crates[move_to] += crates[move_from][len(crates[move_from])-amount:]
        crates[move_from] = crates[move_from][:len(crates[move_from])-amount]

#Print Answer
for i in range(len(crates)):
    print(crates[i+1])
