# input file에서 입력 받기
import sys
sys.stdin = open("input.txt", "r")

# 정수 입력 받기
N = int(input())

# 구분된 문자 한 줄에 입력 받기
input().split()

# 구분된 정수 한 줄에 입력 받기
N, M = map(int, input().split())

# 1차원 리스트 입력 받기
arr = list(map(int, input().split()))

# 1차원 리스트 문자 입력 받기
arr = list(input()) # 1234 => ['1', '2', '3', '4']

# 1차원 리스트 숫자 입력 받기
arr = list(map(int, input())) # 1234 => [1, 2, 3, 4]

# 2차원 리스트 입력 받기
N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

# ---------------------------------

arr = []
for i in range(n):
  arr.append(list(map(int, input().split())))

# 2차원 리스트 초기화
arr = [[0] * M for _ in range(N)]