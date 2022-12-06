file = open('Day 6\input1.txt')
data = file.readline()
file.close()

start_of_packet = ''
skipped_chars = 0

# You can easily change the problem by changing this var here. 
# Part 1 asks for 4 distinct characters, part 2 asks for 14
len_of_message = 14

for c in data:
    if len(start_of_packet) != len_of_message:
        start_of_packet += c
    else:
        skipped_chars += 1
        start_of_packet = start_of_packet[1:] + c
        
        if not set(i for i in start_of_packet if start_of_packet.count(i)>1):
            print('break point')
            break

print(skipped_chars + len(start_of_packet))