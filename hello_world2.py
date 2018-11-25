"""
Created today bby
@author: XML34
"""

from listaDiccionarios import *
import pandas as pd
import sys
from mpi4py import MPI

#word = input('introduce la palabra entre comillas: ')
def top10():
	comm = MPI.COMM_WORLD
	#print ('My rank is', comm.rank)
	lista1=[]
	lista2=[]
	lista3=[]
	if comm.rank == 1:
	    #print ('Doing the task of rank 1')
	    art1=pd.read_csv('../../../opt/datasets/articles1.csv',header=0)
	    listaDiccionarios(art1)
	    lista1=listaDiccionarios.searchTop10(sys.argv[1])

	if comm.rank == 2:
	    #print ('Haciendo la tarea del nodo 2')
	    art2=pd.read_csv('../../../opt/datasets/articles2.csv',header=0)
	    listaDiccionarios(art2)
	    lista2=listaDiccionarios.searchTop10(sys.argv[1])


	if comm.rank == 3:
	    #print ('faisant noeud de devoirs 3')
	    art3=pd.read_csv('../../../opt/datasets/articles3.csv',header=0)
	    listaDiccionarios(art3)
	    lista3=listaDiccionarios.searchTop10(sys.argv[1])

	return lista1,lista2,lista3


l1,l2,l3=top10()
print("lista 1: ",l1)

