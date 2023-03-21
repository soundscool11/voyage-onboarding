import sys, math
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

a, b = map(int, input().split())

gcd = math.gcd(a, b)
print(gcd)
print(a * b // gcd)