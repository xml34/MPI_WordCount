"""
Created today bby
@author: XML34
"""

from listaDiccionarios import *
import pandas as pd
import numpy as np
import sys
from mpi4py import MPI

#word = input('introduce la palabra entre comillas: ')
def top10():
	#print (sys.argv[1])
	lista1=[]
	lista2=[]
	lista3=[]
	if comm.rank == 1:
	    #print ('Doing the task of rank 1')
	    art1=pd.read_csv('../../../opt/datasets/articles1.csv',header=0)
	    lD=listaDiccionarios(art1)
	    lista1=lD.searchTop10()

	if comm.rank == 2:
	    #print ('Haciendo la tarea del nodo 2')
	    art2=pd.read_csv('../../../opt/datasets/articles2.csv',header=0)
	    lD=listaDiccionarios(art2)
	    lista2=lD.searchTop10()


	if comm.rank == 3:
	    #print ('faisant noeud de devoirs 3')
	    art3=pd.read_csv('../../../opt/datasets/articles3.csv',header=0)
	    lD=listaDiccionarios(art3)
	    lista3=lD.searchTop10()

	return lista1,lista2,lista3

comm = MPI.COMM_WORLD
l1,l2,l3=top10()
if comm.rank == 1:
	print("csv 1: ",np.array(l1))

if comm.rank == 2:
	print("csv 2: ",np.array(l2))

if comm.rank == 3:
	print("csv 3: ",np.array(l3))

