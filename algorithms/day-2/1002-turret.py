import sys, time, math
start_time = time.time()
sys.stdin = open("input.txt", "r")

T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = math.sqrt(((x1-x2)**2 + (y1-y2)**2)) #두명 사이 거리
    if distance == 0 and r1 == r2: # 두 원이 위치, 반지름 같은 원일때
        print(-1)
    elif abs(r1-r2) == distance or r1+r2 == distance: # 두 원이 내접/외접할때
        print(1)
    elif abs(r1-r2)< distance < (r1+r2): # 두 원이 서로다른 두점에서 만날때
        print(2)
    else:
        print(0)

print (math.sqrt(26))
print(int(26**0.5))

5.0990195135927845
5

end_time = time.time()
print("\nTime:", round(end_time - start_time, 5))
