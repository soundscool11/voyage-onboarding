import sys, time
start_time = time.time()
sys.stdin = open("input.txt", "r")

input = sys.stdin.readline

cnt = int(input()) # n의 약수의 갯수
arr = list(map(int, input().split())) # n의 약수

min = min(arr)
max = max(arr)
print(min*max)

end_time = time.time()
print("\nTime:", round(end_time - start_time, 5))