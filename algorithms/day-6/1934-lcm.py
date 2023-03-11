import sys, time, math
start_time = time.time()
sys.stdin = open("input.txt", "r")

input = sys.stdin.readline

# 최대 공약수, 최소 공배수, 유클리드 호제법
# 최소 공배수 => x*y // 최대 공약수
N = int(input())

def gcd(x, y): # 재귀 함수 말고 반복문
    if x < y :
        x, y = y, x
    while y != 0:
        tmp = x%y
        x, y = y, tmp
    return x

for _ in range(N):
    x, y = map(int, input().split())
    print(x * y // gcd(x, y)) 
    
end_time = time.time()
print("\nTime:", round(end_time - start_time, 5))

# 유클리드 호제법

# def lcm(x, y):
#     value = x*y // gcd(x,y)
#     return value


# def gcd2(x, y):
#     if x < y :
#         x, y = y, x
#     while y != 0:
#         tmp = x%y
#         x, y = y, tmp
#     return x