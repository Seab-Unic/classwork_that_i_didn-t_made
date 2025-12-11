import random
import time
tic = time.perf_counter()
n = int(input("длина списка - "))
s = [random.randint(1, 148) for _ in range(n)]
s.sort()
s_double = s.copy()
k = int(input("ваше число - "))
def insert_sorted(s_double, k):
    for i in range(len(s_double)):
        if s_double[i] > k:
            s_double.insert(i, k)
            break
    else:
        s_double.append(k)
    return s_double
s_double = insert_sorted(s_double, k)
toc = time.perf_counter()
print(f"Время выполнения: {toc - tic} секунд")
print(s_double)
