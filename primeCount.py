# Damian Mietus
# Reddit Daily Programmer
# Challenge #359 [Hard] Primes in Grids
# Completed September 24

# Prime Number Counter 
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
			
			i = i + 1
	
		intSize = intSize + 1	
	
	return pnFound
	
def	getVerticalLine(grid, number, i):
	tempVertical = ""
	tempStr = ""
	for j in range (0, number):
		tempStr = grid[j]
		tempVertical = tempVertical + tempStr[i]	

	return tempVertical
	
def getRightDiagonal(grid, number, start):
	tempDiag = ""
	tempStr = ""
	j = 0
	for i in range (start, number):
		tempStr = grid[i]
		tempDiag = tempDiag + tempStr[j]
		j = j + 1
	return tempDiag
	
def getRightDiagonalExpr(grid, number, start, offSet):
	j = offSet
	temp = ""
	for i in range (0, number):
		str = grid[i]
		if j < number:
			temp = temp + str[j]
		j = j + 1
	return temp
	
def getLeftDiagonal(grid, number, start):
	tempDiag = ""
	tempStr = ""
	j = number-1
	for i in range (start, number):
		tempStr = grid[i]
		tempDiag = tempDiag + tempStr[j]
		j = j - 1
	return tempDiag
	
def getLeftDiagonalExpr(grid, number, start, offSet):
	j = offSet
	temp = ""
	for i in range (0, number):
		str = grid[i]
		if j >= 0:
			temp = temp + str[j]
		j = j - 1
	return temp
		
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

primeNumbersInt = primeNumberFinder(9999)
primeNumbersStr = []

for item in primeNumbersInt:
	primeNumbersStr.append(str(item))

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

#Diagonal
tempRightDiagonal = getRightDiagonal(pnGrid, number, 0)
primeNumbersFound = countPrimeLine(tempRightDiagonal, primeNumbersFound, primeNumbersStr, number);
tempReverse = reverseString(tempRightDiagonal)
primeNumbersFound = countPrimeLine(tempReverse, primeNumbersFound, primeNumbersStr, number);

#Check from center to down-left 
for i in range(0, number):
	tempRightDiagonal = getRightDiagonal(pnGrid, number, i)
	primeNumbersFound = countPrimeLine(tempRightDiagonal, primeNumbersFound, primeNumbersStr, number);	
	tempReverse = reverseString(tempRightDiagonal)
	primeNumbersFound = countPrimeLine(tempReverse, primeNumbersFound, primeNumbersStr, number);
	
#Check from center to up-right 	
for i in range(0, number):
	tempRightDiagonal = getRightDiagonalExpr(pnGrid, number, i-1, i+1)
	primeNumbersFound = countPrimeLine(tempRightDiagonal, primeNumbersFound, primeNumbersStr, number);
	tempReverse = reverseString(tempRightDiagonal)
	primeNumbersFound = countPrimeLine(tempReverse, primeNumbersFound, primeNumbersStr, number);

tempLeftDiagonal = getLeftDiagonal(pnGrid, number, 0)
primeNumbersFound = countPrimeLine(tempLeftDiagonal, primeNumbersFound, primeNumbersStr, number);
tempReverse = reverseString(tempLeftDiagonal)
primeNumbersFound = countPrimeLine(tempReverse, primeNumbersFound, primeNumbersStr, number);

#Check from right to down-right 
for i in range(0, number):
	tempLeftDiagonal = getLeftDiagonal(pnGrid, number, i)
	primeNumbersFound = countPrimeLine(tempLeftDiagonal, primeNumbersFound, primeNumbersStr, number);
	tempReverse = reverseString(tempLeftDiagonal)
	primeNumbersFound = countPrimeLine(tempReverse, primeNumbersFound, primeNumbersStr, number);
	
#Check from right to up-left
for i in range(0, number-1):
	tempLeftDiagonal = getLeftDiagonalExpr(pnGrid, number, i-1, i+1)
	primeNumbersFound = countPrimeLine(tempLeftDiagonal, primeNumbersFound, primeNumbersStr, number);
	tempReverse = reverseString(tempLeftDiagonal)
	primeNumbersFound = countPrimeLine(tempReverse, primeNumbersFound, primeNumbersStr, number);

	
print ("Total Unique Prime Numbers: ", len(primeNumbersFound))
print (primeNumbersFound)