import time
import threading
import numpy as np
from concurrent.futures import as_completed, ProcessPoolExecutor

point_num = 10000000
process_num = 6

point_per_process = point_num//process_num
argv = [point_per_process]*process_num


def get_pi(rand_point_num):
    data = np.random.uniform([0, 0], [1, 1], [rand_point_num, 2])
    return(
        len(list(filter(lambda x: x[0]**2+x[1]**2 < 1, data))))


# process pool
if __name__ == '__main__':
    time_start = time.time()
    with ProcessPoolExecutor(max_workers=process_num) as pool:
        pi = sum(list(pool.map(get_pi, argv)))*4/point_num
    time_end = time.time()
    print(pi)
    print('process pool Time Spend', time_end-time_start, 's')
