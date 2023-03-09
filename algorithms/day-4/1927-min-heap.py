import sys, time, heapq
start_time = time.time()
sys.stdin = open("input.txt", "r")

input = sys.stdin.readline

heap = []
heapq.heapify(heap)

N = int(input())
for _ in range(N):
    x = int(input())
    if x == 0:
        if len(heap) < 1:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, x)


end_time = time.time()
print("\nTime:", round(end_time - start_time, 5))