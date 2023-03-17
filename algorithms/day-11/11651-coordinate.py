import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())
lst = []
for _ in range(n):
    lst.append(list(map(int, input().split())))
lst.sort(key=lambda x: (x[1], x[0]))
for x, y in lst:
    print(x, y)
