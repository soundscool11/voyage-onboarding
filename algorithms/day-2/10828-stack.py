import sys, time
start_time = time.time()
sys.stdin = open("input.txt", "r")


N = int(input())
stack = []

for _ in range(N):
    order = list(sys.stdin.readline().split())
    if order[0] == 'push':
        stack.append(order[1])
    elif order[0] == 'size':
        print(len(stack))
    elif order[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif order[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif order[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
          print(stack[-1])

end_time = time.time()
print("\nTime:", round(end_time - start_time, 5))