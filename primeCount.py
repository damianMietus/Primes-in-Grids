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
	i = 0
	for i in range
		
	
	
#Main
i = 0
j = 0
digitFlag = True
number = int(input("Enter a number for the Prime Grid: "));
grid = [[0 for x in range(number)] for y in range(number)]
for i in range(0, number):
	grid[i] = int(input(""));
	#print (digitCounter(grid[i]))
	if digitCounter(grid[i]) != number:		
		digitFlag = False
		while (digitFlag == False):
			invalidDigitCountError(number)
			grid[i] = int(input(""));
			if digitCounter(grid[i]) == number:
				digitFlag = True
		
		
print (grid)
