class diccionario:
	ide=None
	tittle=None
	count=None
	
	def __init__(self,text,ide,tittle,palabra):
		d={}
		self.ide=ide
		self.tittle=tittle

		for char in '-.,\n':
			text=text.replace(char,' ')
		text = text.lower()
		word_list=text.split()

		for word in word_list:
			d[word] = d.get(word, 0) + 1
		self.count=d["house"]


	def getId(self):
		return self.ide

	def getTittle(self):
		return self.tittle

	def getCount(self):
		return self.count
