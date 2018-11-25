import pandas as pd
from diccionario import * #.getId .getTittle .getCount

class listaDiccionarios:

	dicionarios=[]



	def __init__(self,csv):
		contenidos=csv['content']
		tittles=csv['tittle']
		ide=csv['id']

		for i in range(len(ide)):
			self.diccionarios.append(diccionario(contenidos[i],ide[i],tittle[i]))
		#return self.diccionarios

	def searchTop10(self,word):
		diccionarios=[]
		for dic in self.diccionarios:
			diccionarios.append([dic.getId(),dic.getTittle(),dic.getCount(word)])
		diccionarios.sort(key=lambda x:x[2], reverse=True)
		return diccionarios[:10]






