import sys, time
start_time = time.time()
sys.stdin = open("input.txt", "r")

input = sys.stdin.readline

# 20 + 40 - 60 + 25 + 66 - 30 + 100
# - 뒤에는 다더해야되 다음 - 전까지 
# - 기준으로 split 해주고 -> 대총 콘솔 찍으면서 연산해주면 될거같은데용

#1. 마이너스 기준으로 스플릿한다
#2. [맨처음 항목은 무조건 +]
#3. 플러스 부호인 항목 모두를 더한것에 마이너스 부호인 항목 모두 더한것을 빼준다
sik = input()
#1. 마이너스 기준으로 스플릿한다
result=sik.split('-')
#['55+30' / '50+40', '40', '40+50']

fin=sum(list(map(int, result[0].split('+'))))
for i in range(1,len(result)): 
    fin -= sum(list(map(int, result[i].split('+'))))

print(fin)

end_time = time.time()
print("\nTime:", round(end_time - start_time, 5))