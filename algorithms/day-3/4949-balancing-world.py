import sys, time
start_time = time.time()
sys.stdin = open("input.txt", "r")

# 1. 스택에 (), [] 넣어가면서 판별
# 2. 문자열이 '.' 일때 종료
while True:
    sentence = input()
    stack = []
    flag = True

    if sentence == '.':
        break
    for s in sentence:
        # 여는 괄호 일 때
        if s == '(' or s == '[':
            stack.append(s)
        # 닫는 소괄호
        elif s == ')':
            if len(stack) < 1:
                flag = False
                break
            if stack[-1] != '(':
                flag = False
                break
            stack.pop()
        # 닫는 대괄호
        elif s == ']':
            if len(stack) < 1:
                flag = False
                break
            if stack[-1] != '[':
                flag = False
                break
            stack.pop()
    if len(stack) != 0 or flag == False:
        print('no')
    else:
        print('yes')

        # print('stack: ', stack)

        

end_time = time.time()
print("\nTime:", round(end_time - start_time, 5))