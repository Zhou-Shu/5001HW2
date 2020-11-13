# serial

import numpy as np
import time


def serial_pi(step):
    time_start = time.time()
    delta = 1/step
    x = np.linspace(0, 1, step)
    pi = 0
    for i in x:
        pi += delta*4/(1+i**2)
    print(pi)
    time_end = time.time()
    print('Serial Time Spend', time_end-time_start, 's')


serial_pi(1000000)
