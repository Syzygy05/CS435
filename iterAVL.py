class Node:
	def __init__(self, data):
		self.value = data
		self.leftChild = None
		self.rightChild = None
		self.height = 1	

class AVL:
	def __init__(self):
		self.root = None

	def insertIter(self, currNode, data):
		if self.root == None:
			self.root = Node(data)
			return
		
		while True:
			subTreeRoot = currNode
			if data < currNode.value:
				currNode = currNode.leftChild
				if currNode == None:
					subTreeRoot.leftChild = Node(data)
					return
			elif data > currNode.value:
				currNode = currNode.rightChild
				if currNode == None:
					subTreeRoot.rightChild = Node(data)
					return 

		currNode.height = max(currNode.leftChild.height, currNode.rightChild.height)

		balanceFactor = currNode.leftChild.height - currNode.rightChild.height

		# RR
		if data < currNode.leftChild.value and balanceFactor > 1:
			tempNode = currNode.leftChild
			currNode.leftChild = currNode.leftChild.rightChild
			currNode.leftChild.rightChild = tempNode

			currNode.leftChild.height = max(currNode.leftChild.leftChild.height, currNode.leftChild.rightChild.height) + 1
			currNode.height = max(currNode.leftChild.height, currNode.rightChild.height) + 1

			return currNode.leftChild

		# LR
		if data > currNode.rightChild.data and balanceFactor < -1:
			tempNode = currNode.rightChild
			currNode.rightChild = currNode.rightChild.leftChild
			currNode.rightChild.leftChild = tempNode

			currNode.rightChild.height = max(currNode.rightChild.leftChild.height, currNode.rightChild.rightChild.height) + 1
			currNode.height = max(currNode.leftChild, currNode.rightChild) + 1

			return currNode.rightChild




		if data > currNode.leftChild.value and balanceFactor > 1:
			tempNode = currNode.rightChild
			currNode.rightChild = currNode.rightChild.leftChild
			currNode.rightChild.leftChild = tempNode

			currNode.rightChild.height = max(currNode.rightChild.leftChild.height, currNode.rightChild.rightChild.height) + 1
			currNode.height = max(currNode.leftChild, currNode.rightChild) + 1

			currNode.leftChild = currNode.rightChild

			tempNode = currNode.leftChild
			currNode.leftChild = currNode.leftChild.rightChild
			currNode.leftChild.rightChild = tempNode

			currNode.leftChild.height = max(currNode.leftChild.leftChild.height, currNode.leftChild.rightChild.height) + 1
			currNode.height = max(currNode.leftChild.height, currNode.rightChild.height) + 1

			return currNode.leftChild

		if data < currNode.rightChild.value and balanceFactor < -1:
			tempNode = currNode.leftChild
			currNode.leftChild = currNode.leftChild.rightChild
			currNode.leftChild.rightChild = tempNode

			currNode.leftChild.height = max(currNode.leftChild.leftChild.height, currNode.leftChild.rightChild.height) + 1
			currNode.height = max(currNode.leftChild.height, currNode.rightChild.height) + 1

			currNode.rightChild = currNode.leftChild

			tempNode = currNode.rightChild
			currNode.rightChild = currNode.rightChild.leftChild
			currNode.rightChild.leftChild = tempNode

			currNode.rightChild.height = max(currNode.rightChild.leftChild.height, currNode.rightChild.rightChild.height) + 1
			currNode.height = max(currNode.leftChild, currNode.rightChild) + 1

			return currNode.rightChild

	def deleteIter(self, root, data):
		pass

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


















