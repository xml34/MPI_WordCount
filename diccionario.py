class diccionario:
	ide=None
	tittle=None
	d={}
	
	def __init__(self,text,ide,tittle):
		x={}
		self.ide=ide
		self.tittle=tittle

		for char in '-.,\n':
			text=text.replace(char,' ')
		text = text.lower()
		word_list=text.split()

		for word in word_list:
			self.x[word] = self.x.get(word, 0) + 1
		self.d=x

	def getId(self):
		return self.ide

	def getTittle(self):
		return self.tittle

	def getCount(self,word):
		return self.d[word]
