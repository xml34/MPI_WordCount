import pandas as pd
from diccionario import * #.getId .getTittle .getCount

class listaDiccionarios:
	diccionarios=[]


	def __init__(self,csv):
		contenidos=csv['content']
		tittles=csv['title']
		ide=csv['id']
		for i in range(len(ide)):
			self.diccionarios.append(diccionario(contenidos[i],ide[i],tittles[i]))
			print(self.diccionarios[i][0])
			print(self.diccionarios[i][1])
			print(self.diccionarios[i][2])
		#return self.diccionarios

	def searchTop10(self,word):
		diccionarios=[]
		for dic in self.diccionarios:
			diccionarios.append([dic.getId(),dic.getTittle(),dic.getCount(word)])
		diccionarios.sort(key=lambda x:x[2], reverse=True)
		return diccionarios[:10]







