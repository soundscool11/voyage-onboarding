import sys, time
start_time = time.time()
sys.stdin = open("input.txt", "r")

input = sys.stdin.readline

# 제일큰거 몫 > 0: -> cnt += 1 -> value %= 몫
N, K = map(int, input().split())
arr = []
count = 0
for _ in range(N):
    arr.append(int(input()))


for i in range(N-1, -1, -1):
    if K >= arr[i]:
        count += K // arr[i]
        K = K % arr[i]
print(count)
    
end_time = time.time()
print("\nTime:", round(end_time - start_time, 5))