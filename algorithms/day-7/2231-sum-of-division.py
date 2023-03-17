import sys, math
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

def digit_length(n):
    return int(math.log10(n) + 1 if n else 0)

n = int(input())
m = 0
digit = digit_length(n)

for i in range(n):
    val = i
    cnt_val = i
    for j in range(digit, 0, -1):
        cnt_val += i // (10 ** (j - 1))
        i = i % (10 ** (j - 1))
    if cnt_val == n:
        m = val
        break

print(m)