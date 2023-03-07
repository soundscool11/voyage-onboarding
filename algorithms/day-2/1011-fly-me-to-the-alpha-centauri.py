import sys, time
start_time = time.time()
sys.stdin = open("input.txt", "r")

T = int(sys.stdin.readline())
for _ in range(T):
    x, y = map(int, sys.stdin.readline().split())
    distance = y-x
    number = 0 # 블록 개수 
    while True:
        if distance <= number*(number+1): # 거리가 블록수보다 작으면 탈출해서 개수세기로 넘어감
            break
        number += 1 # 거리가 블록보다 크면 다음블록으로 넘어감
    if distance <= number ** 2: # 거리가 제곱블록보다 작으면
        print(number*2-1) # 홀수 출력
    else:
        print(number*2) # 아니면 짝수 출력


end_time = time.time()
print("\nTime:", round(end_time - start_time, 5))


# 1          1 1**2 
# 11         2 1*2 1블록
# 111        3           2제곱블록
# 121          2**2 
# 1211       4           2짝수블록
# 1221         2*3 2블록
# 12211      5
# 12221      
# 12321        3**2
# 123211     6
# 123221     
# 123321       3*4 3블록
# 1233211    7
# 1233221    
# 1233321    
# 1234321      4**2

# 4*5