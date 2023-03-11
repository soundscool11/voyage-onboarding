def isValid(self, s):
    s = [str(s) for s in s]
    isCorr = True
    stack = []
    for p in s:
        if p == '(' or p == '{' or p == '[':
            stack.append(p)
        elif p == ')':
            if len(stack) == 0:
                isCorr = False
                break
            if stack[-1] == '(':
                stack.pop()
            else:
                isCorr = False
                break
        elif p == '}':
            if len(stack) == 0:
                isCorr = False
                break
            if stack[-1] == '{':
                stack.pop()
            else:
                isCorr = False
                break
        elif p == ']':
            if len(stack) == 0:
                isCorr = False
                break
            if stack[-1] == '[':
                stack.pop()
            else:
                isCorr = False
                break
    
    if isCorr and len(stack) == 0:
        return 'true'
    else:
        return 'false'
    
print(isValid(0, '(]'))