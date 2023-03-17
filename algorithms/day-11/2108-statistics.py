import sys, collections
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())
num_lst = []
for _ in range(n):
    num_lst.append(int(input()))
num_lst.sort()


# 산술평균
print(round(sum(num_lst) / n))
# 중앙값
print(num_lst[n//2])
# 최빈값
most = collections.Counter(num_lst).most_common(2)
if len(most) > 1 and most[0][1] == most[1][1]:
    print(most[1][0])
else:
    print(most[0][0])
# 범위
print(num_lst[-1]-num_lst[0])

