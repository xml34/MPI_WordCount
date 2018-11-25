import pandas as pd
from diccionario import * #.getId .getTittle .getCount

class listaDiccionarios:
	diccionarios=[]


	def __init__(self,csv):
		contenidos=csv['content']
		tittles=csv['title']
		ide=csv['id']
		dic=None
		for i in range(len(ide)):
			dic=diccionario(contenidos[i],ide[i],tittles[i])
			print("-->",dic.getCount("house"))
			self.diccionarios.append(dic)
			dic=None

		#return self.diccionarios

	def searchTop10(self,word):
		diccionarios=[]
		for dic in self.diccionarios:
			diccionarios.append([dic.getId(),dic.getTittle(),dic.getCount(word)])
		diccionarios.sort(key=lambda x:x[2], reverse=True)
		return diccionarios[:10]







