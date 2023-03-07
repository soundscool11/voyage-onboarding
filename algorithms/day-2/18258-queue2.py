import sys, time
start_time = time.time()
sys.stdin = open("input.txt", "r")
from collections import deque
N = int(input())
queue = deque([])

for _ in range(N):
    order = list(sys.stdin.readline().split())
    if order[0] == 'push':
        queue.append(order[1])
    elif order[0] == 'size':
        print(len(queue))
    elif order[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif order[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
            queue.popleft()
    elif order[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif order[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])

end_time = time.time()
print("\nTime:", round(end_time - start_time, 5))