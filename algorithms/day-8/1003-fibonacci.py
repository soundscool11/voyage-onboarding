import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    cnt_zero = [1, 0]
    cnt_one = [0, 1]

    for i in range(2, N+1):
        cnt_zero.append(cnt_zero[i-1] + cnt_zero[i-2])
        cnt_one.append(cnt_one[i-1] + cnt_one[i-2])
    
    print(cnt_zero[N], cnt_one[N])
