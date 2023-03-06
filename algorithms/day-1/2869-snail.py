# 문제
# 땅 위에 달팽이가 있다. 이 달팽이는 높이가 V미터인 나무 막대를 올라갈 것이다.

# 달팽이는 낮에 A미터 올라갈 수 있다. 하지만, 밤에 잠을 자는 동안 B미터 미끄러진다. 또, 정상에 올라간 후에는 미끄러지지 않는다.

# 달팽이가 나무 막대를 모두 올라가려면, 며칠이 걸리는지 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 세 정수 A, B, V가 공백으로 구분되어서 주어진다. (1 ≤ B < A ≤ V ≤ 1,000,000,000)

# 출력
# 첫째 줄에 달팽이가 나무 막대를 모두 올라가는데 며칠이 걸리는지 출력한다.

# output: 4

import sys, time, math
start_time = time.time()
sys.stdin = open("input.txt", "r")

A, B, V = map(int, input().split())
# A만큼 올라가고 B만큼 미끄러지므로 사실상 하루에 A - B만큼 올라감
# 다 올라간 날은 미끄러지지 않으므로 V - A가 최종 목표 높이
# count값은 소수값이 나오므로 ceil을 통해 반올림 처리
count = (V - A) / (A - B)
result = math.ceil(count) + 1

print(result)

# target = 0
# while V != target:
#     target += A
#     if target >= V:
#         count += 1
#         break
#     else:
#         target -= B
#         count += 1
# print(count) # 예제 3번에서 시간이 너무 오래걸림

end_time = time.time()
print("\nTime:", round(end_time - start_time, 5))