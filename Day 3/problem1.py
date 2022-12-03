file = open("input1.txt")
text = file.readlines()
file.close()

def find_common_letter(left_string, right_string):
    for c in left_string:
        if c in right_string:
            return c

sum_of_priorities = 0

for bag in text:
    bag = bag[0:len(bag)-1]
    n = len(bag)
    letter = find_common_letter(bag[0:n//2], bag[n//2:])

    sum_of_priorities += (ord(letter)-96) if letter.islower() else (ord(letter.lower())-96+26)

print(sum_of_priorities)