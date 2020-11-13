# mpiexec -n 5 python MSDM5001\ring.py

from mpi4py import MPI
import numpy as np

Np = 5  # number of nodes, must smeller than the np within mpiexec command
num_of_loop = 50  # number of iterations

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

# create a 1-dim ring topology

dims = [Np]
periods = [True]
ring_comm = comm.Create_cart(dims, periods)
shift_node = ring_comm.Shift(0, 1)
loop_counter = 0
counter = loop_counter

if(rank == 0):
    wt = MPI.Wtime()

while counter <= num_of_loop-1:
    if (rank == 0):
        loop_counter += 1
        ring_comm.send(loop_counter, dest=shift_node[1], tag=1)
        counter = ring_comm.recv(source=shift_node[0], tag=1)
        print('node %d pass a message from node %d to node %d [loop counter: %d]' %
              (rank, shift_node[0], shift_node[1], counter))
    else:
        counter = ring_comm.recv(source=shift_node[0], tag=1)
        ring_comm.send(counter, dest=shift_node[1], tag=1)
        print('node %d pass a message from node %d to node %d [loop counter: %d]' %
              (rank, shift_node[0], shift_node[1], counter))

if(rank == 0):
    wt = MPI.Wtime() - wt
    print("Time spend: %fs" % (wt))
