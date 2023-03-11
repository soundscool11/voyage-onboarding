import sys, time
start_time = time.time()
sys.stdin = open("input.txt", "r")

input = sys.stdin.readline

N = int(input())
times = list(map(int, input().split()))
# 3 1 4 3 2
# 1 2 3 3 4

# 1. 오름차순 정렬
# 2. 누적합 만들면서 cnt += 

times.sort()
cnt = 0
section_sum = 0
for i in range(0, N):
    section_sum += times[i]
    cnt += section_sum

print(cnt)
    
end_time = time.time()
print("\nTime:", round(end_time - start_time, 5))

# 1
# 12
# 123
# 1233
# 12334 
# 1 * 5(N) + 2 * 4 + 3 * 3 + 3 * 2 + 4 * 1   -> 같은 인덱스를 왼편은 +

n = int(input())
timing = map(int, input().split())
time = sorted(timing)
result = 0
for i in range(n):
    result = result + (len(time)-i) * time[i]
print(result)