"""
Created today bby
@author: XML34
"""
from mpi4py import MPI
import pandas as pd

art1=pd.read_csv('articles1.csv',header=0)
art2=pd.read_csv('articles2.csv',header=0)
art3=pd.read_csv('articles3.csv',header=0)

comm = MPI.COMM_WORLD

print ('My rank is', comm.rank)
if comm.rank == 1:
    print ('Doing the task of rank 1')

if comm.rank == 2:
    print ('Haciendo la tarea del nodo 2')

if comm.rank == 3:
    print ('faisant noeud de devoirs 3')
