# 상근이는 요즘 설탕공장에서 설탕을 배달하고 있다. 상근이는 지금 사탕가게에 설탕을 정확하게 N킬로그램을 배달해야 한다. 
# 설탕공장에서 만드는 설탕은 봉지에 담겨져 있다. 봉지는 3킬로그램 봉지와 5킬로그램 봉지가 있다.
# 상근이는 귀찮기 때문에, 최대한 적은 봉지를 들고 가려고 한다. 

# 예를 들어, 18킬로그램 설탕을 배달해야 할 때, 3킬로그램 봉지 6개를 가져가도 되지만, 
# 5킬로그램 3개와 3킬로그램 1개를 배달하면, 더 적은 개수의 봉지를 배달할 수 있다.

# 상근이가 설탕을 정확하게 N킬로그램 배달해야 할 때, 봉지 몇 개를 가져가면 되는지 그 수를 구하는 프로그램을 작성하시오.

# 상근이가 배달하는 봉지의 최소 개수를 출력한다. 만약, 정확하게 N킬로그램을 만들 수 없다면 -1을 출력한다.

# input = 18, output = 4
# input = 4, output = -1
# input = 27, output = 7


import sys, time
start_time = time.time()
sys.stdin = open("input.txt", "r")

N = int(input())

max = N // 5
bag = 0
flag = 0

for i in range(0, max):
  bag = (N // 5) - i
  rest = N - (bag * 5)
  if rest % 3 == 0:
    bag += rest // 3
    flag = 1
    break
  
if flag == 0:
  if N % 3 == 0:
    bag = N // 3
  else:
    bag = -1

print(bag)

end_time = time.time()
print("\nTime:", round(end_time - start_time, 5))