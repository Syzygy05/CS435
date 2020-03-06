class Node:
	def __init__(self, data):
		self.value = data
		self.leftChild = None
		self.rightChild = None	


class binarySearchTree:

	def __init__(self):
		self.root = None
		self.dataList = []

	def insertIter(self, currNode, data):
		if self.root == None:
			self.root = Node(data)
			self.dataList.append(self.root)
			return
		
		while True:
			subTreeRoot = currNode
			if data < currNode.value:
				currNode = currNode.leftChild
				if currNode == None:
					subTreeRoot.leftChild = Node(data)
					self.dataList.append(Node(data))
					return
			elif data > currNode.value:
				currNode = currNode.rightChild
				if currNode == None:
					subTreeRoot.rightChild = Node(data)
					self.dataList.append(Node(data))
					return 



	def deleteIter(self, root, data):
		if root == None:
			print('Tree is empty')

		parent = None
		currNode = root


		while currNode != None:
			parent = currNode

			if data < currNode.value:
				currNode =currNode.leftChild
			else:
				currNode = currNode.rightChild

		if currNode.leftChild == None and currNode.rightChild == None:
			if parent.leftChild == currNode:
				parent.leftChild == None
			else:
				parent.rightChild == None
		elif currNode.leftChild != None and currNode.rightChild != None:
			replacementNode = self.findNextRec()
			root = replacementNode
		else:
			replacementNode = None
			if currNode.leftChild != None:
				replacementNode = currNode.leftChild
			else:
				replacementNode = currNode.rightChild

			if currNode == parent.leftChild:
				parent.leftChild = replacementNode
			else:
				parent.rightChild = replacementNode





	def findNextIter(self):
		rightSubTree = self.root.rightChild
		while rightSubTree.leftChild != None:
			rightSubTree = rightSubTree.leftChild

		return rightSubTree

	def findPrevIter(self):
		leftSubTree = self.root.leftChild
		while leftSubTree.rightChild != None:
			leftSubTree = leftSubTree.rightChild

		return leftSubTree

	def findMinIter(self):
		currNode = self.root
		while currNode.leftChild != None:
			currNode = currNode.leftChild

		return currNode

	def findMaxIter(self):
		currNode = self.root
		while currNode.rightChild != None:
			currNode = currNode.rightChild

		return currNode






tree = binarySearchTree()



tree.insert(tree.root, 50)
tree.insert(tree.root, 35)
tree.insert(tree.root, 75)
tree.insert(tree.root, 25)
tree.insert(tree.root, 85)
tree.insert(tree.root, 45)












