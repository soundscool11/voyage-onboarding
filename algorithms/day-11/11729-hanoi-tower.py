import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())

#  hanoi(n, start, mid, target):
#   hanoi(n-1, start, target, mid):
#   1에서 타겟 print(start, target)
#   hanoi(n-1  mid start target)
cnt=0
def hanoi(n, start, mid, target):
    global cnt
    if n == 1:
        cnt+=1
        print(start, target)
        return
    hanoi(n-1, start, target, mid) # n-1까지의 원판을 mid로 이동
    hanoi(1, start, mid, target)
    #print(start, target) # 가장 큰 원판이 target으로 옮겨갈 때 print
    hanoi(n-1, mid, start, target) # mid에 있는 원판들을 target으로 이동

print(2**n-1)
hanoi(n, 1, 2, 3)
print('cnt: ', cnt)