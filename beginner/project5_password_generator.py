import random

alphabet_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

number_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

special_char_list = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_',
                     '=', '+', '[', ']', '{', '}', '|', ':', ';', '"', "'",
                     '<', '>', ',', '.', '?', '/', '`', '~']

num_alphabets = int(input())
num_nos = int(input())
num_sc = int(input())

list = []

for i in range(0, num_alphabets):
    list.append(random.choice(alphabet_list))

for j in range(0, num_nos):
    list.append(random.choice(number_list))

for k in range(0, num_sc):
    list.append(random.choice(special_char_list))

random.shuffle(list)

ans = ""

for data in list:
    ans += data

print(ans)
