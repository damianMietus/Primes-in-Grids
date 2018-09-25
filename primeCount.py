# Prime Number Counter 
# This change was done with Github Desktop
def primeNumberFinder(size):
    pnArray = [2, 3, 5]
    i = 7;
    j = 0;
    pnFlag = True
    for i in range (7, size):      
      pnFlag = True
      for j in range(0, len(pnArray)-1):      
        if i%pnArray[j] == 0:
          pnFlag = False
          break
        j+1 
      if pnFlag == True:
        pnArray.append(i)
      i + 2
    return pnArray

def digitCounter(number):
	digits = 0
	while (number > 0):
		digits = digits + 1
		number = number//10
	return digits

def invalidDigitCountError(integer):
	print ("invalid entry. You're input must have", integer, "digits in length. Please input again: ")
	return
	
def reverseString(string):
	return string[::-1]
    
def countPrimeLine(line, pnFound, pnList, size):
	i = 0
	intSize = 1
	addBool = True
	while (intSize < size+1):
		
		for i in range(0, size-intSize+1):
			#print ("i = ", i)
			#get the part of line to check
			temp = line[i:i+intSize]
			addBool = True
			
			#check if it is not in our prime list
			if temp in str(pnFound):
				addBool = False
				
			#check if our number is prime
			if addBool == True:
				if temp in pnList:
					pnFound.append(temp)
					#print("Found one")
			
			i = i + 1
	
		intSize = intSize + 1
		#print ("Reached the end of the while loop")
	
	
	return pnFound
	
def	getVerticalLine(grid, number, i):
	tempVertical = ""
	tempStr = ""
	for j in range (0, number):
		tempStr = grid[j]
		tempVertical = tempVertical + tempStr[i]	

	return tempVertical
	
def getRightDiagonal(grid, number):
	tempDiag = ""
	tempStr = ""
	j = 0
	for i in range (0, number):
		tempStr = grid[i]
		tempDiag = tempDiag + tempStr[j]
		j = j + 1
	return tempDiag
	
def getLeftDiagonal(grid, number):
	tempDiag = ""
	tempStr = ""
	j = number-1
	for i in range (0, number):
		tempStr = grid[i]
		tempDiag = tempDiag + tempStr[j]
		j = j - 1
	return tempDiag
		
#Main
i = 0
j = 0
digitFlag = True
number = int(input("Enter a number for the Prime Grid: "));
grid = [[0 for x in range(number)] for y in range(number)]
for i in range(0, number):
	grid[i] = int(input(""));
	if digitCounter(grid[i]) != number:		
		digitFlag = False
		while (digitFlag == False):
			invalidDigitCountError(number)
			grid[i] = int(input(""));
			if digitCounter(grid[i]) == number:
				digitFlag = True
		


pnGrid = []		
for item in grid:
	pnGrid.append(str(item))
print (pnGrid)




primeNumbersInt = primeNumberFinder(9999)
primeNumbersStr = []
for item in primeNumbersInt:
	primeNumbersStr.append(str(item))

#print (primeNumbersStr)

primeNumbersFound = []
tempVertical = ""
tempRightDiagonal = ""
for i in range (0, number):
	#Horizontal
	primeNumbersFound = countPrimeLine(pnGrid[i], primeNumbersFound, primeNumbersStr, number);
	tempReverse = reverseString(pnGrid[i])
	primeNumbersFound = countPrimeLine(tempReverse, primeNumbersFound, primeNumbersStr, number);
	
	#Vertical
	tempVertical = getVerticalLine(pnGrid, number, i)
	primeNumbersFound = countPrimeLine(tempVertical, primeNumbersFound, primeNumbersStr, number);
	tempReverse = reverseString(tempVertical)
	primeNumbersFound = countPrimeLine(tempReverse, primeNumbersFound, primeNumbersStr, number);
	

	print("Vertical = ", tempVertical)
	

#Diagonal
tempRightDiagonal = getRightDiagonal(pnGrid, number)
primeNumbersFound = countPrimeLine(tempRightDiagonal, primeNumbersFound, primeNumbersStr, number);
#print("Right Diag =", tempRightDiagonal)
tempReverse = reverseString(tempRightDiagonal)
primeNumbersFound = countPrimeLine(tempReverse, primeNumbersFound, primeNumbersStr, number);
#Check from center to up-right 
#for i in range(0, number):

tempLeftDiagonal = getLeftDiagonal(pnGrid, number)
primeNumbersFound = countPrimeLine(tempLeftDiagonal, primeNumbersFound, primeNumbersStr, number);
#print("Left Diag =", tempLeftDiagonal)
tempReverse = reverseString(tempLeftDiagonal)
primeNumbersFound = countPrimeLine(tempReverse, primeNumbersFound, primeNumbersStr, number);

#primeNumbersFound = countPrimeLine(pnGrid[0], primeNumbersFound, primeNumbersStr, number);
#primeNumbersFound = countPrimeLine(pnGrid[1], primeNumbersFound, primeNumbersStr, number);

print ("Total Unique Prime Numbers: ", len(primeNumbersFound))
print (primeNumbersFound)