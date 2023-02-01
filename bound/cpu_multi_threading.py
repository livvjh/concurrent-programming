import os
import threading
import time
from concurrent.futures import ThreadPoolExecutor
import sys

sys.set_int_max_str_digits(0)

nums = [50, 63, 32]


def cpu_bound_func(num):
    print(f'{os.getpid()} process | {threading.get_ident()} thread', {num})
    numbers = range(1, num)
    total = 1
    for i in numbers:
        for j in numbers:
            for k in numbers:
                total *= i * j * k
    return total


def main():
    executor = ThreadPoolExecutor(max_workers=10)
    executor.map(cpu_bound_func, nums)

if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(end - start) # cpu bound의 경우 동시성과 구현으로는 차이가 없다
