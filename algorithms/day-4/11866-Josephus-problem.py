import sys, time
from collections import deque
start_time = time.time()
sys.stdin = open("input.txt", "r")

input = sys.stdin.readline

n, k = map(int, input().split())

dq = deque()
result = []

for i in range(n):
    dq.append(i+1)

while len(dq) != 0:
    dq.rotate(-k+1)
    result.append(dq.popleft())

result = (', '.join([str(num) for num in result]))
print(f"<{result}>")


end_time = time.time()
print("\nTime:", round(end_time - start_time, 5))