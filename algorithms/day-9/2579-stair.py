import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())
steps = []
mem = [0] * n

for _ in range(n):
    steps.append(int(input()))

if n == 1:
    print(steps[0])

elif n == 2:
    print(steps[0]+steps[1])

else:
    mem[0] = steps[0]
    mem[1] = steps[0] + steps[1]
    mem[2] = max(steps[0] + steps[2], steps[1] + steps[2])

    for i in range(3, n):
        mem[i] = max(mem[i-3] + steps[i-1] + steps[i], mem[i-2] + steps[i])

    print(mem[n-1])