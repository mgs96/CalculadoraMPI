#Divide un numero enorme entre un entero
import numpy
from mpi4py import MPI

import sys


comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

n = float(sys.argv[1])/(size - 1)
n1 = float(sys.argv[2])


if (rank != 0):
	resta = n/n1
	comm.send(resta, dest=0, tag=11)
else:
	cont = 0;
	for i in range(1, size):
		total = comm.recv(source=i, tag=11)
		cont = cont + total
	print cont

n = comm.bcast(n, root=0)
n1 = comm.bcast(n1, root=0)

# un aporte de Nelson Caraballo Ayala
