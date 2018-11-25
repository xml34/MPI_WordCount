# MPI_WordCount
### Integrantes: Daniel Morales Londoño 201510090010

## Intruducción
este proyecto contiene un 3 clases las cuales leen tres documentos a través de 
la librería pandas y de cada uno aplica streaming para calcular
cuales son los 10 registros que más contiene cierta palabra ingresada

## Como funciona
la clase pricipal se encargar de dividir la tarea en 3 nodos.
cada nodo hace una instancia de listaDiccionarios.

la clase listaDiccionarios se encarga de crear un arreglo de
objetos dicionario

la clase diccionario recive cada fila del archivo leido por el nodo
y se aplica un word count, luego según la palabra ingresada, se calcula
la cantidad de veces que se repite en dicha fila

una véz termina cada uno de los nodos, la clase listaDiccionarios ordena
la lista entorno a la columna que contiene la cantidad palabras encontradas
por parrafo y la clase principal recibe los primeros 10
de cada nodo y los imprime en pantalla

## Como Correr

1.	se ingresa a la carpeta MPI_WordCount
2.	se corre el siguiente comando
	mpiexec -f hosts_mpi -n 4 /opt/anaconda3/bin/python hello_world2.py <<palabra>>
	ejemplo:
	mpiexec -f hosts_mpi -n 4 /opt/anaconda3/bin/python hello_world2.py korea





