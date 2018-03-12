import string
import random

line = "methinks it is like a weasel"
line_len = len(line)
alphabet = string.ascii_lowercase + " "
monkey = ""
save_array = ""


def line_generator(len_of_line, monkey_line):   #generating a original_line
    for i in range(len_of_line):
        monkey_line += random.choice(alphabet)
    return monkey_line


def similarity_check(original_line, len_of_line, monkey_line):  #cheking similarity
    similarity = 0
    for i in range(len_of_line):
        if original_line[i] == monkey_line[i]:
            similarity += 1
    return similarity


maximum_maximum = 0
for i in range(100000000000):
    temp1 = line_generator(line_len, monkey)
    temp2 = similarity_check(line, line_len, temp1)
    maximum = 0
    if temp2 > maximum:
        save_array = temp1
        maximum = temp2
    if temp2 > maximum_maximum:
        maximum_maximum = temp2
    print(save_array)
    print(temp2)
print(maximum_maximum)



