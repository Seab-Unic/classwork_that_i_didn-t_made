import random
import time
tic = time.perf_counter()
n = int(input("длина списка - "))
s = [random.randint(1, 148) for _ in range(n)]
s.sort()
s_double = s
k = int(input("ваше число - "))
s_double.append(k)
s_double.sort()
toc = time.perf_counter()
print(f"Время выполнения: {toc - tic} секунд")
print(s_double)
#насколько я помню вы кажется запреали так делать но я неуверен,другого решения в голову не приходит
