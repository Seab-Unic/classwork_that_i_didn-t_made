import random
import time
tic = time.perf_counter()
n = int(input("длина списка - "))
s = [random.randint(1, 148) for _ in range(n)]
s.sort()
s_double = s
k = int(input("ваше число - "))
def binary_search(s, k, s_double):
    low = 0
    high = len(s) - 1
    while low <= high:
        middle = (low + high) // 2
        if s[middle] == k:
            s_double.insert(middle, k)
            return
        elif s[middle] > k:
            high = middle - 1
        else:
            low = middle + 1
    s_double.insert(low, k)
binary_search(s, k, s_double)
toc = time.perf_counter()
print(f"Время выполнения: {toc - tic} секунд")
print(s_double)
