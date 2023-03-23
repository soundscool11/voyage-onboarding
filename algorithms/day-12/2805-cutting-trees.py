import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n, m = map(int, input().split())
h = list(map(int, input().split()))
start, end = 1, max(h)

while start <= end:
    mid = (end + start) // 2
    total = 0
    for i in range(n):
        if h[i] > mid:
            total += h[i] - mid

    if total >= m:
        start = mid + 1
        result = mid
    elif total < m:
        end = mid - 1

print(result)