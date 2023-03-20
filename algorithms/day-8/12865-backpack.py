import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

# Knapsack Algorithm

N, K = map(int, input().split())
stuff = [[0, 0]]
knapsack = [[0] * (K+1) for _ in range(N+1)]
for _ in range(N):
    stuff.append(list(map(int, input().split())))

for i in range(1, N+1):
    for j in range(1, K+1):
        w = stuff[i][0]
        v = stuff[i][1]

        if j < w:
            knapsack[i][j] = knapsack[i-1][j]
        else:
            knapsack[i][j] = max(knapsack[i-1][j], knapsack[i-1][j-w]+v)
