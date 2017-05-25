#Carlos Montes - Suma
import sys
from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

def suma(lista):
	suma=0
	n = len(lista)
	i=1
	while(i <= n):
		suma = suma + long(lista.pop())
		i=i+1
	print suma

# n numero de procesos, ejemplo de cadena: 84+31+67, m numero de terminos
# g numero de elementos por grupo
def separar_terminos(cadena,n):
	m=0
	cadena=cadena.split("+")
	m=len(cadena)
	g=m//n
	cad=[]
	sl=[]
	if(n <= (m//2) and n > 1):
		i=1
		j=1
		while(i < n):
			sl=[]
			while(j <= g):
				sl.append(cadena.pop())
				j=j+1
			j=1
			cad.append(sl)
			i=i+1
		sl=[]
		k=1
		t=len(cadena)
		s = m - t - 1

		while(k <= s):
			sl.append(cadena.pop())
			k=k+1
		cad.append(sl)
	else:
		print "El n(numero procesos) debe ser > 1 y n <= ",str(m//2)," si son un m(numero de terminos) de ",m
	return cad


if __name__ == "__main__":
	
	tam=len(sys.argv)
	e=1
	cade=""
	while(e < tam):
		if(e == tam-1):
			cade=cade+str(sys.argv[e])
		else:
			cade=cade+str(sys.argv[e])+"+"
		e=e+1

	print ""
	print cade
	suma = 0
	
	if rank == 0:
   		data=separar_terminos(cade,int(size))
   		print ""
   		print 'we will be scattering:',data
	else:
   		data = None

	data = comm.scatter(data, root=0)
	
	n=len(data)
	f=1
	while(f <= n):
		suma = suma + long(data[f-1])
		f=f+1
	
	data=0
	data=long(suma)
	print ""
	print 'rank',rank,'has data:',data

	newData = comm.gather(data,root=0)

	sumax=0
	q=len(newData)
	f=1
	while(f <= q):
		sumax = sumax + long(newData[f-1])
		f=f+1

	if rank == 0:
		print ""
		print 'Resultado:',sumax
		print ""