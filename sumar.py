#suma un numero enorme entre un entero
import numpy
from mpi4py import MPI
from decimal import *

import sys


comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

n = Decimal(sys.argv[1])
n1 = Decimal(sys.argv[2])/(size - 1)

if (rank != 0):
	nTemp = comm.recv(source=0, tag=10)
	resta = nTemp + n1
	comm.send(resta, dest=0, tag=11)
else:
	cont = n;
	for i in range(1, size):
		comm.send(cont, dest=i, tag=10)
		total = comm.recv(source=i, tag=11)
		cont = total
	print cont

# un aporte de Nelson Caraballo Ayala