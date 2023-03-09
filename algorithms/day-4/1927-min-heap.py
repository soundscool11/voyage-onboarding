import sys, time
start_time = time.time()
sys.stdin = open("input.txt", "r")



end_time = time.time()
print("\nTime:", round(end_time - start_time, 5))