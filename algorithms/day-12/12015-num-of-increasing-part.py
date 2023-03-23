import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())
cases = list(map(int, input().split()))
lst = [0]

for case in cases:
    if lst[-1] < case:
        lst.append(case)

    else:
        start = 0
        end = len(lst)

        while start < end:
            mid = (start + end) // 2
            if lst[mid] < case:
                start = mid + 1
            else:
                end = mid
        lst[end] = case

print(len(lst) - 1)
