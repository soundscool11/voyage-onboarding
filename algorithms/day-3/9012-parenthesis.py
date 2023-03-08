import sys, time
start_time = time.time()
sys.stdin = open("input.txt", "r")

N = int(input())

for _ in range(N):
    stack = 0
    gwalhos = input()
    for gwalho in gwalhos:
        if gwalho == '(':
            stack += 1
        if gwalho == ')':
            stack -= 1
        if stack < 0:
            break 
    if stack != 0:
        print('NO')
    else:
        print('YES')

# N = int(input())
# for _ in range(N):
#     S = input()
#     while '()' in S:
#         S = S.replace('()','')
#     if S == '':
#         print("YES")
#     else:
#         print("NO")

end_time = time.time()
print("\nTime:", round(end_time - start_time, 5))