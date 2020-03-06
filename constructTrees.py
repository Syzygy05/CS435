import random
import time

class Node:
	def __init__(self, data):
		self.value = data
		self.leftChild = None
		self.rightChild = None
		self.height = 1	

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
					self.insertRec(currNode, data)
			elif data > currNode.value:
				if currNode.rightChild == None:
					currNode.rightChild = Node(data)
					self.dataList.append(currNode.rightChild)
					#print('3inserted node ' + str(data))
				else:
					currNode = currNode.rightChild
					self.insertRec(currNode, data)


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


# iterative AVL tree starts here
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


arr10k = getRandomArray(50000)

bst = BinarySearchTree()

avl = AVL()

start_time = time.time()
for num in arr10k:
	bst.insertRec(bst.root, num)
	avl.insertIter(avl.root, num)
print("--- %s seconds ---" % (time.time() - start_time))



















