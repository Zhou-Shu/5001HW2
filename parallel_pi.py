# parallel
# mpiexec -n 5 python MSDM5001\parallel_pi.py

from mpi4py import MPI
import numpy as np


def multiprocess_pi(step):
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    if rank == 0:
        wt = MPI.Wtime()

    # split the task
    index_start = (rank*step)//size
    index_end = ((rank+1)*step)//size
    delta = 1/step
    x = np.linspace(0, 1, step)
    pi = 0

    for i in x[index_start:index_end]:
        pi += delta*4/(1+i**2)

    # reduce by the sum operator
    pi = comm.reduce(pi, op=MPI.SUM, root=0)
    if rank == 0:
        print(pi)
        wt = MPI.Wtime() - wt
        print("Parallel Time spend: %f s with %d processes" % (wt, size))


multiprocess_pi(1000000)
