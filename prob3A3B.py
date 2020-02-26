# Problem 3a

import random

def getRandomArray(n):
	randomArr = []

	for i in range(n):
		randNum = random.randint(0, 100000)
		if randNum not in randomArr:
			randomArr.append(randNum)

	return randomArr


# Problem 3b
def getSortedArray(n):
	sortArr = []

	for i in range(n, 0, -1):
		sortArr.append(i)

	return sortArr




print(getRandomArray(10))
print(getSortedArray(10))