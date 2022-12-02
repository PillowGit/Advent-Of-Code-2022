
file = open('input1.txt')
text = file.readlines()

most_calories = [3,2,1]
current_calories = 0

def compare_top_three(calories):
    most_calories.append(calories)
    most_calories.remove(min(most_calories))
    # most_calories.sort()
    # most_calories.pop(0)

for entry in text:
    if entry == '\n':
        compare_top_three(current_calories)
        current_calories = 0
    else:
        current_calories += int(entry[0:len(entry)-1])

print(sum(most_calories))

file.close()