import sys
sys.stdin = open("input.txt", "r")

S = input().lower()
alphabet = [-1] * 26
count = 0

for i in S:
    index = ord(i) - 97
    if alphabet[index] == -1:
        alphabet[index] = count
    count += 1

for char in alphabet:
    print(char, end=" ")

# Clean code

# def get_idx(word):
#     result = [-1]*len(string.ascii_lowercase)
#     for i in range(len(word)):
#         idx = ord(word[i]) - 97
#         if result[idx] == -1:
#             result[idx] = i
#     print(' '.join([str(num) for num in result]))