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
    
def countPrimeHorizontalLine(line, pnFound, pnList, size):
	addBool = True
	tempLine = line
	while (tempLine > 0.5):
		print(tempLine)
		addBool = True
		if tempLine in pnFound:
			addBool = False
		if addBool == True:
			if tempLine in pnList:
				print("adding", tempLine, "To the list")
				pnFound.append(tempLine)
		
		tempLine = int(tempLine/10)
		
		
			'''
	i = 0
	intSize = 1
	addBool = True
	while (intSize < size+1):
		
		for i in range(0, size-intSize+1):
			print ("i = ", i)
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
					print("Found one")
			
			i = i + 1
	
		intSize = intSize + 1
		print ("Reached the end of the while loop")
		
	
	
	return pnFound
	'''
		
	return pnFound	
		
	
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
		
		
print (grid)




primeNumbers = primeNumberFinder(999)
print (primeNumbers)

primeNumbersFound = []
primeNumbersFound = countPrimeHorizontalLine(grid[0], primeNumbersFound, primeNumbers, number);
print (primeNumbersFound)
