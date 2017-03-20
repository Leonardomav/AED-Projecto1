import csv
from operator import itemgetter 	#testing this

csv.register_dialect('AED', delimiter=';') #registers a new dialect, separated with ";", instead of the default ","

def loadCsvToArray():
	#loads the csv file into an array of arrays, 1
	with open('dados.csv','r') as file: 			#opens the csv file
		reader = csv.reader(file, dialect='AED')	
		countries = stackCountries()
		iterator = 0
		for row in reader:							#iterates the file
			years = stackYears()	#iterates the row and gets the stuff that matters

			for i in range(2, len(row)):

				if row[i] != '':
					years.push(tuple([int(i + 1958), float(row[i])]))

			countries.push(CountryNode(row[0], row[1] , years))
			if iterator == 0:
				countries.pop()
			iterator = 1
	
	file.close()									#closes the file since we don't need it open anymore
	return countries									#returns the stack

class stackCountries:
	def __init__(self):
		self.items = []		#each item == CountryNode() 

	def is_empty(self):
		return self.items == []
	
	def push(self, item):
		self.items.insert(0, item)

	def pop(self):
		return self.items.pop(0)

	def peek(self):
		return self.items[0]

	def size(self):
		return len(self.items)

	def invert(self, stackF): 	#stackF = Final (inverted)
		if self.size() > 0:			#if stack is not empty
			stackF.push(self.pop())	#ads to the aux stack the first elem of self
			return self.invert(stackF)	#calls the function itself
		else:
			self.items = stackF.items
			

class CountryNode:
	def __init__(self, cName = None, cCode = None, years = None):
		self.cName = cName 		#str -> e.g. 'Portugal'
		self.cCode = cCode 		#str -> e.g. 'PRT'
		self.years = years 		#class -> stackYears()

	def getCountryName(self):	#self explanatory
		return self.cName

	def getCountryCode(self):	#self explanatory
		return self.cCode

	def getYears(self):			#set explanatory
		return self.years

	def setCountryName(self, cName):	#self explanatory
		self.cName = cName

	def setCountryCode(self, cCode):	#self explanatory
		self.cCode = cCode

	def setYears(self, years):			#self explanatory
		self.years = years

class stackYears:
	def __init__(self):
		self.items = []

	def is_empty(self):
		return self.items == []

	def push(self, item):
		self.items.insert(0, item)

	def pop(self):
		return self.items.pop(0)

	def peek(self):
		return self.items[0]

	def size(self):
		return len(self.items)

if __name__ == '__main__':
	stack = loadCsvToArray()
	stack.invert(stackCountries())
	print(stack.peek().cName)
	print(stack.peek().cCode)
	print(stack.peek().years.peek())