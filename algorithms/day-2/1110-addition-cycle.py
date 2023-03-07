import sys, time
start_time = time.time()
sys.stdin = open("input.txt", "r")

M = int(input())
N = M
count = 0

while True:
    first = N // 10
    second = N % 10

    num = first + second
    num = num % 10
    N = 10 * second + num
    count += 1
    
    if N == M:
        break

print(count)

end_time = time.time()
print("\nTime:", round(end_time - start_time, 5))