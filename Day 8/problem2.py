file = open("Day 8\input.txt")
lines = file.readlines()
file.close()

matrix = [[int(s) for s in line[:-1]] for line in lines]
height = len(matrix)
width = len(matrix[0])

def walk(ls, target):
    for x in range(len(ls)):
        if ls[x] >= target:
            return x + 1
    return len(ls)

def generate_score(row, column):
    value = matrix[row][column]
    lr = matrix[row].copy()
    ud = [matrix[x][column] for x in range(height)]
    directions = [ lr[0:column][::-1], lr[column+1:], ud[0:row][::-1], ud[row+1:] ]
    score = 1
    while [] in directions: directions.remove([])
    for direction in directions:
        score *= walk(direction, value)
    return score
    

best_score = 0

# all insides
for a in range(1,width-1):
    for b in range(1,height-1):
        best_score = max(best_score, generate_score(a,b))
# vertical edges
for row in range(height):
    best_score = max(best_score, generate_score(row,0), generate_score(row,width-1))
# horizontal edges
for column in range(width):
    best_score = max(best_score, generate_score(0, column), generate_score(height-1,column))

print(best_score)