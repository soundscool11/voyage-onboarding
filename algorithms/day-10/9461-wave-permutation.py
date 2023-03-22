import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

tri = [0 for i in range(101)]
tri[1] = 1
tri[2] = 1
tri[3] = 1

for i in range(4, 101):
    tri[i] = tri[i-3] + tri[i-2]

T = int(input())

for _ in range(T):
    N = int(input())
    print(tri[N])
