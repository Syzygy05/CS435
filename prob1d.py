def insertRec(root, data):
	while True:
		if root.data == None:
			root.data = data
			return root
		else:
			currentNode = root

		if data < currentNode.data:
			currentNode = currentNode.left
			if currentNode.data == None:
				currentNode.data = data
				return root

# A bit lost on delete and insert. 
# The recursion implementation is much more simple.

def deleteRec(data):
	pass

def findNextRec(node):
	currentNode = node.data
		while currentNode.right != None:
			currentNode = currentNode.left
			currentNodeData = currentNode.data
		return currentNodeData

def findPrevRec(node):
	currentNode = node.data
		while currentNode.left != None:
			currentNode = currentNode.right
			currentNodeData = currentNode.data
		return currentNodeData

def findMinRec(root):
	if root == null:
		return 'Tree is empty'
	while root.left != None
		node = root.left
	return node.data

def findMaxrec(root):
	if root == null:
		return 'Tree is empty'
	while root.right != None
		node = root.right
	return node.data