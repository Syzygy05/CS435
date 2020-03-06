import random
import time

class Node:
	def __init__(self, data):
		self.value = data
		self.leftChild = None
		self.rightChild = None	
		self.height = 1	


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


# ____________________________________________________________________-

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




# Random functions start here

def getRandomArray(n):
	randomArr = []

	count = 0
	for i in range(n):
		randNum = random.randint(0, 1000000000000)
		if randNum not in randomArr:
			print(count)
			count += 1
			randomArr.append(randNum)

	return randomArr


# Problem 3b
def getSortedArray(n):
	sortArr = []

	for i in range(n, 0, -1):
		sortArr.append(i)

	return sortArr


arr10k = getRandomArray(10000)

bst = binarySearchTree()

avl = AVL()

start_time = time.time()
for num in arr10k:
	bst.insertIter(bst.root, num)
	avl.insertIter(avl.root, num)
print("--- %s seconds ---" % (time.time() - start_time))






















