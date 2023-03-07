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
