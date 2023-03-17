import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n, m = map(int, input().split())
cards = list(map(int, input().split()))

cards.sort(reverse=True)
sum = 0
list = []

for i in range(n-2):
    sum = cards[i]
    for j in range(i+1, n-1):
        sum += cards[j]
        for k in range(j+1, n):
            sum += cards[k]
            if sum <= m:
                list.append(sum)
            sum -= cards[k]
        sum -= cards[j]

print(max(list))