import sys, time
start_time = time.time()
sys.stdin = open("input.txt", "r")
# 1. 1부터 10000 -> for 문을돈다
# 2. str(i)=>  666 in string
# 3. 만들어둔 666 list에 integer로 추가 len(666_list) == n이랑 같아지면
# 666list[-1]
input = sys.stdin.readline


n = int(input()) # >> 760ms
six_lst = []
cnt = 1
while True:
    if '666' in str(cnt):
        six_lst.append(cnt)
    if len(six_lst) == n:
        break
    cnt += 1

print(six_lst[-1])
    
end_time = time.time()
print("\nTime:", round(end_time - start_time, 5))



# n의 범위가 [1~ 10000]

# # 리스트로 모든경우 만들기 >> 런타임에러(IndexError)
# lst = [666]
# for i in range(1, 10):
#     if i == 6:
#         for j in range(10):
#             lst.append(6660 + j)
#     else:
#         lst.append(i * 1000 + 666)
# n = int(input())
# print(lst[n-1]) >> 취소


# 카운트로 풀어 보기 >> 900ms
n = int(input())
cnt = 0
number = 665
while cnt != n:
    number += 1
    string = str(number)
    if '666' in string:
        cnt += 1
print(int(number))