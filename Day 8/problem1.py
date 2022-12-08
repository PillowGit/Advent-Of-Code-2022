file = open("Day 8\input.txt")

matrix = [[int(s) for s in line[:-1]] for line in file.readlines()]
height = len(matrix)
width = len(matrix[0])
file.close()

def is_visible(row, column):
    value = matrix[row][column]
    lr = matrix[row].copy()
    ud = [matrix[x][column] for x in range(height)]
    return min(max(lr[0:column]), max(lr[column+1:]), max(ud[0:row]), max(ud[row+1:])) < value

visible = 2*height + 2*width - 4

for a in range(1,width-1):
    for b in range(1,height-1):
        if is_visible(a,b): 
            visible += 1

print(visible)