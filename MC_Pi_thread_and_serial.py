import time
import threading
import numpy as np
from concurrent.futures import ThreadPoolExecutor, as_completed

# limited improvement
# thread pool is suitable for I/O operations, but not for this
# as the Python kernel only allows one thread to execute at a time
# Also, the filter function within serial program already is a SIMD

point_num = 10000000
thread_num = 6

point_per_thread = point_num//thread_num
argv = [point_per_thread]*thread_num


def get_pi(rand_point_num):
    data = np.random.uniform([0, 0], [1, 1], [rand_point_num, 2])
    return(
        len(list(filter(lambda x: x[0]**2+x[1]**2 < 1, data))))

# thread pool


time_start = time.time()
with ThreadPoolExecutor(max_workers=thread_num) as pool:
    pi = sum(list(pool.map(get_pi, argv)))*4/point_num
time_end = time.time()
print(pi)
print('Thread pool Time Spend', time_end-time_start, 's')


# serial code

time_start = time.time()
pi = get_pi(point_num)*4/point_num
time_end = time.time()
print(pi)
print('Serial Time Spend', time_end-time_start, 's')
