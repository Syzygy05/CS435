class Node:
    def __init__(self, num):
        self.num = num
        self.left = None
        self.right = None


class BST:
	def __init__(self):
		self.root = None


	def insertRec(node, num):
		if root == None:
			root = Node(num)
			return root
		elif num < root.num:
			root.left = insertRec(root.left, num)
		elif num > root:
			root.right = insertRec(root.right, num)

		return root

	def deleteRec(root, num):
		# Does the opposite traversal that you would do in insertRec
		if root == None:
			return 'Tree is empty!'
		elif root < num:
			root.right = deleteRec(root.right, num)
		elif root > num:
			root.left = deleteRec(root.left, num)
		else:
			if root.right == None:
				return root.left
			elif root.left = None:
				return root.right
			else:
				root.num = findNext(root.right)
				root.right = deleteRec(root.right, root.num)
				return root
		
		if root.left = None 

	def findNextRec(node):
		currentNode = node.data
		if currentNode.right != None:
			currentNode = findNextRec(currentNode.left)
		return currentNode


	def findPrevRec(node):
		currentNode = node.data
		if currentNode.left != None:
			currentNode = findNextRec(currentNode.right)
			return findMaxrec()

	def findMinRec(root):
		if root == null:
			return 'Tree is empty'
		elif root.left != None:
			node = findMinRec(root.left)
			return node.data

	def findMaxrec(root):
		if root == null:
			return 'Tree is empty'
		elif root.right != None:
			node = findMinRec(root.right)
			return node.data


'''
i) 	This question is simply asking us how we would implement these functions
	critical to the use of a Binary Search Tree through recursive algorithms. 

	Assumptions: 
	1) I am assumming that the class definitions have already been defined.
	2) I am also assumming that no duplicate num values will be passed to 
	the tree 

ii)	For insert, I've ensured that a root already exists. Also, you have to 
	make sure that you are not inserting a node that already exists.

	For delete, the function will warn you that you are attempting to delete
	from an empty tree. 

	For findPrev/findNext/findMin/findMax, an edge case would be if the tree 
	is empty. For findPrev and findNext, if there is only one node in the 
	tree, (the root), then there exists no other node that will satisfy these 
	functions. Null needs to programmed in to the method. 

iii) See attached pdf

iv)	Create an algorithm for each method. (Does not need to be submitted)

v)	Time and space are always something that is at the forethought when using
	recursion to computer something. If the tree is very large, we will keep 
	making recursive calls for all of these methods. 

vi)	See code 

vii) I'm not quite sure what problems I could run into other than my recursion
	 is wrong and therefore I will run into space issues or incorrect answers.
	 I suppose a seg fault is the result then.
'''














