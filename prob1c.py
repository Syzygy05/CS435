class Node:
	def __init__(self, data):
		self.value = data
		self.leftChild = None
		self.rightChild = None

class BinarySearchTree:

	def __init__(self):
		self.root = None
		self.dataList = []


	def insertRec(self, currNode, data):
		# If the Root is non-existent, then added node as root
		if self.root == None:
			self.root = Node(data)
			self.dataList.append(self.root)
			#print('1inserted node ' + str(data))
		else:
			if data < currNode.value:
				if currNode.leftChild == None:
					currNode.leftChild = Node(data)
					self.dataList.append(currNode.leftChild)
					#print('2inserted node ' + str(data))
				else:
					currNode = currNode.leftChild
					self.insert(currNode, data)
			elif data > currNode.value:
				if currNode.rightChild == None:
					currNode.rightChild = Node(data)
					self.dataList.append(currNode.rightChild)
					#print('3inserted node ' + str(data))
				else:
					currNode = currNode.rightChild
					self.insert(currNode, data)


	def deleteRec(self, root, data):
		if self.root == None:
			print('Tree is empty')

		if root == None:
			return root
		elif data < root.value:
			root.leftChild = self.delete(root.leftChild, data)
		elif data > root.value:
			root.rightChild = self.delete(root.rightChild, data)
		else:
			if root.leftChild == None:
				return root.rightChild
			elif root.rightChild == None:
				return root.leftChild

			root = self.findNextRec(root.rightChild)
			root.rightChild = self.delete(root.rightChild, root.value)

		return root


		'''
		if self.root.leftChild == None and self.root.rightChild == None:
			self.root = None
		elif self.root.leftChild != None and self.root.rightChild == None:
			self.root = self.root.leftChild
			self.root.leftChild = None
		elif self.root.leftChild == None and self.root.rightChild != None:
			self.root = self.root.rightChild
			self.root.rightChild = None
		else:
			replacementNode = self.findNextRec(node)
			node = replacementNode
			
			
		# Need to find the next largest number from the root and replace
		# The leftmost node in the right subtree from the root
		'''

	def findNextRec(self, node):
		if node == None:
			print('Tree is empty')
		elif node.rightChild != None:
			node = self.findMinRec(node.rightChild)

		return node

			

	def findPrevRec(self, node):
		if node == None:
			print('Tree is empty')
		elif node.leftChild != None:
			node = self.findMaxRec(node.leftChild)

		return node
		

	def findMinRec(self, node):
		if node == None:
			print('Tree is empty.')
		elif node.leftChild != None:
			node = self.findMinRec(node.leftChild)

		return node


	def findMaxRec(self, node):
		if node == None:
			print('Tree is empty.')
		elif node.rightChild != None:
			node = self.findMaxRec(node.rightChild)

		return node



'''

tree = binarySearchTree()



tree.insert(tree.root, 50)
tree.insert(tree.root, 35)
tree.insert(tree.root, 75)
tree.insert(tree.root, 25)
tree.insert(tree.root, 85)
tree.insert(tree.root, 45)




print(tree.delete(tree.root, 35).value)


'''


















