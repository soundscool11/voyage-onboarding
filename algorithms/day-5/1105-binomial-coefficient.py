import sys, time, collections, itertools
start_time = time.time()
sys.stdin = open("input.txt", "r")


input = sys.stdin.readline
n, k = map(int, input().split())


def factorial(n):
    answer = 1
    for i in range(1, n+1):
        answer *= i
    return answer

# def factorial_recursion(n):
#     if n == 1:
#         return 1
#     return n * factorial_recursion(n-1)

# itertools.combination()
# itertools.permutations()
# collections.Counter(arr).most_common()
# collections.defaultdict / collections.OrderedDict[입력 순서대로 저장]
# enumerate

# arr = [i for i in range(n)]
# print(len(list(itertools.combinations(arr, k))))

print(factorial(n)//(factorial(k)*(factorial(n-k))))


end_time = time.time()
print("\nTime:", round(end_time - start_time, 5))