import sys, time
start_time = time.time()
sys.stdin = open("input.txt", "r")

from collections import deque

# 회전하는큐 
n, m = map(int, input().split())
targets = list(map(int, input().split()))
que = deque(i for i in range(1, n+1))
cnt = 0

#  1. 같으면 빼주기
# 2. 다르면, -> 왼쪽이야? 오른쪽이야?

for target in targets:
    while que[0] != target:
        if que.index(target) < round(len(que)) / 2:
            que.rotate(-1)
            cnt += 1
        else:
            que.rotate(1)
            cnt += 1
    que.popleft()

print(cnt)

end_time = time.time()
print("\nTime:", round(end_time - start_time, 5))