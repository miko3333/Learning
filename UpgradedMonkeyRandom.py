import string
import random


def line_generator(len_of_line, monkey_line):
    for i in range(len_of_line):
        if save_line[i] == line[i]:
            save_line[i] = save_line[i]
        else:
            monkey_line[i] = random.choice(alphabet)
    return monkey_line


line = list("methinks it is like a weasel")
line_len = len(line)
alphabet = string.ascii_lowercase + " "
save_line = list()
for i in range(line_len):
    save_line.append(random.choice(alphabet))

while save_line != line:
    print(line_generator(line_len, save_line))

