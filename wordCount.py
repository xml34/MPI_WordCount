import sys

d={}
def dictionary(text):
	word_freq = []

	for char in '-.,\n':
		text=text.replace(char,' ')
	text = text.lower()

	#print('text')#print(text)	

	word_list=text.split()

	#print('word_list')#print(word_list)

	for word in word_list:
		d[word] = d.get(word, 0) + 1

	print('d')
	print(d["coco"])




text='compadre vendame un coco, compadre no vendo coco, como poco coco como, poco coco compro'
dictionary(text)
"""
for key,value in d.items():
	word_freq.append((value,key))

word_freq.sort(reverse=True)

print('word_freq')
print(word_freq[0])
#print(word_freq)
"""
