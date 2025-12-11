import random
import time
tic = time.perf_counter()
n = int(input("длина списка - "))
s = [random.randint(1, 148) for _ in range(n)]
s.sort()
s_double = s
k = int(input("ваше число - "))
def recursive(s_double, k, index=0):
    if index == len(s_double):
        s_double.append(k)
        return s_double
    if s_double[index] > k:
        s_double.insert(index, k)
        return s_double
    return recursive(s_double, k, index + 1)
s_double = recursive(s_double, k)
toc = time.perf_counter()
print(f"Время выполнения: {toc - tic} секунд")
print(s_double)
