file = open('input1.txt')
text = file.readlines()
file.close()

opponent = {
    'A':'rock',
    'B':'paper',
    'C':'scissors'
}
shape_scores = {
    'rock': 1,
    'paper': 2,
    'scissors': 3
}


total = 0

for entry in text:
    # this gives us 'A X\n' so we can take the first three with entry[0:3]
    outcome_score = 0
    if entry[2] == 'X':
        outcome_score = 0
    if entry[2] == 'Y':
        outcome_score = 3
    if entry[2] == 'Z':
        outcome_score = 6
    # Now predict your shape based on the outcome youre given
    op = opponent[entry[0]] # opponents play
    shape_score = 0
    if op == 'rock':
        if outcome_score == 0:
            shape_score = 3
        elif outcome_score == 3:
            shape_score = 1
        else:
            shape_score = 2
    elif op == 'paper':
        if outcome_score == 0:
            shape_score = 1
        elif outcome_score == 3:
            shape_score = 2
        else:
            shape_score = 3
    elif op == 'scissors':
        if outcome_score == 0:
            shape_score = 2
        elif outcome_score == 3:
            shape_score = 3
        else: 
            shape_score = 1
    
    total += outcome_score + shape_score

print(total)