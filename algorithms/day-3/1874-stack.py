import sys, time
start_time = time.time()
sys.stdin = open("input.txt", "r")

N = int(input())
goal = []
stack = []
count = 0
result = []
compare_lst = []
can_stack = True
for i in range(N):
    val = int(input())
    goal.append(val)
    while val > count:
        result.append('+')
        count += 1
        stack.append(count)
    if val == stack[-1]:
        result.append('-')
        stack.pop()
    else:
        can_stack = False
        break

if can_stack == False:
    print('NO')
else:
    print('\n'.join([str(num) for num in result]))
        

end_time = time.time()
print("\nTime:", round(end_time - start_time, 5))