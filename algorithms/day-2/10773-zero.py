import sys, time
start_time = time.time()
sys.stdin = open("input.txt", "r")

K = int(input())
stack = [] # 장부 생성
for _ in range(K):
    n = int(input())
    if n == 0: # 0이면
        stack.pop() # 지우고
    else: # 아니면
        stack.append(n) # 받아적기
print(sum(stack)) # 마지막에 다더하기

end_time = time.time()
print("\nTime:", round(end_time - start_time, 5))