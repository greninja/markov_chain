class TrieNode:
	def __init__(self):
		self.word = None
		self.isend = False
		self.frequency = 0
		self.child_Nodes = {}

	def insert(self,word,pos=0):
		

		current_letter = word[pos]	


		if current_letter not in self.child_Nodes:
			self.child_Nodes[current_letter] = TrieNode()

		if(pos+1 == len(word)):
			self.child_Nodes[current_letter].word = word	
			self.isend = True
			self.frequency += 1	
		else:
			self.child_Nodes[current_letter].insert(word,pos+1)	

		return True

	def getall(self):


		x = {}

		for key,value in self.child_Nodes.iteritems():
			if(value.word is not None):
				x[value.word] = value.frequency


			x.update(value.getall())

		return x		

node = TrieNode()
node.insert("Chandler")
node.insert("Ross")
node.insert("Rachel")
node.insert("Phoebe")
node.insert("Joey")
node.insert("Mpnica")


	
print(node.getall())



