import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n, c = map(int, input().split())
coor = []
for _ in range(n):
    coor.append(int(input()))

coor.sort()
start, end = 1, coor[-1] - coor[0]
result = 0

if c == 2:
    print(end)

else: 
    while start < end:
        mid = (start + end) // 2
        count = 1
        curr = coor[0]
        for i in range(n):
            if coor[i] - curr >= mid:
                count += 1
                curr = coor[i]

        if count >= c:
            start = mid + 1
            result = mid
        elif count < c:
            end = mid

    print(result)
