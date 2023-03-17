import sys
from math import factorial
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

def combinations(n, m):
    return factorial(n) // (factorial(m) * factorial(abs(n-m)))

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(combinations(M, N))