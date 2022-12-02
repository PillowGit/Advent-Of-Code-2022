file = open('input1.txt')
text = file.readlines()
file.close()

opponent = {
    'A':'rock',
    'B':'paper',
    'C':'scissors'
}
response = {
    'X': 'rock',
    'Y': 'paper',
    'Z': 'scissors'
}


total = 0

for entry in text:
    # this gives us 'A X\n' so we can take the first three with entry[0:3]
    outcome_score = 0
    if entry[2] == 'X':
        outcome_score = 1
    if entry[2] == 'Y':
        outcome_score = 2
    if entry[2] == 'Z':
        outcome_score =3
    
    shape_score = 0
    if opponent[entry[0]] == 'rock':
        if entry[2] == 'X':
            shape_score = 3
        elif entry[2] == 'Y':
            shape_score = 6
    elif opponent[entry[0]] == 'paper':
        if entry[2] == 'Y':
            shape_score = 3
        elif entry[2] == 'Z':
            shape_score = 6
    elif opponent[entry[0]] == 'scissors':
        if entry[2] == 'Z':
            shape_score = 3
        elif entry[2] == 'X':
            shape_score = 6
    total += outcome_score + shape_score

print(total)