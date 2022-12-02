
file = open('input1.txt')
text = file.readlines()

most_calories = 0
current_calories = 0

for entry in text:
    if entry == '\n':
        most_calories = max(most_calories, current_calories)
        current_calories = 0
    else:
        current_calories += int(entry[0:len(entry)-1])

print(most_calories)

file.close()