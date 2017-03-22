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
			years = stackYears()					#iterates the row and gets the stuff that matters

			for i in range(2, len(row)):

				if row[i] != '':
					years.push(tuple([int(i + 1958), float(row[i])]))
			years.invert(stackYears())
			countries.push(CountryNode(row[0], row[1] , years))
			if iterator == 0:
				countries.pop()
			iterator = 1
	
	file.close()									#closes the file since we don't need it open anymore
	return countries								#returns the stack

def saveStrutToCSV(stack):
	with open('montDados.csv', 'w') as file:
		#write first row (country name, c code, years)
		file.write('"Country Name"' + ';' + '"Country Code"')
		for i in range(1960, 2017):					#writes the first line
			file.write(';"' + str(i) + '"')


		for i in range(0, stack.size()):			#writes all the data on the stack to the file
			file.write('\n')
			node = stack.pop()						#node (cname, ccode, years stack)
			file.write('"' + node.cName + '";"' + node.cCode + '"')	
			years = node.years 						#years = stack

			for i in range(1960, 2017):				#years we have info on
				file.write(';')
				if years.size() > 0:				#if the stack isn't empty (to avoid error when peek() is used)
					if i == int(years.peek()[0]):
						year = years.pop()			#pops the element
						file.write('"' + str(year[1]) + '"')	#adds it to the file

	return

class stackCountries:
	def __init__(self):
		self.items = []		#each item == CountryNode() 

	def is_empty(self):		#prof
		return self.items == []
	
	def push(self, item):	#prof
		self.items.insert(0, item)

	def pop(self):			#prof
		return self.items.pop(0)

	def peek(self):			#prof
		return self.items[0]

	def size(self):			#prof
		return len(self.items)

	def addCountry(self):
		cName = input('Name of the country to insert:\n>')
		cCode = input('Country code (MAX 3 char):\n>')
		self.push(CountryNode(cName, cCode, stackYears()))	

	def invert(self, stackF): 			#stackF = Final (inverted)
		if self.size() > 0:				#if stack is not empty
			stackF.push(self.pop())		#ads to the aux stack the first elem of self
			return self.invert(stackF)	#calls the function itself
		else:
			self.items = stackF.items

	def concatenate(self, stack):
		for i in range(0, stack.size()):
			self.push(stack.pop())

	def search(self, keyWord, op):	#working
		stackAux = stackCountries()
		for i in range(0, self.size()):
			if keyWord == self.peek().cName or keyWord == self.peek().cCode:
				#do something
				if op == 1:		#add values
					#[DONE]
					self.peek().displayInfo()
					print("\nWhich year do you want to add info about? The years above already have information, if you want to edit it, choose the 'edit value' option in the menu.")
					year = input(">")
					self.peek().addInfo(year)
					break

				elif op == 2:	#edit values
					#[DONE]
					self.peek().displayInfo()
					print("\nWhich year's value do you want to edit?")
					year = input(">")
					self.peek().editInfo(year)
					break	

				elif op == 3:	#remove one value
					#[DONE]
					self.peek().displayInfo()
					print("\nFrom which year do you want to remove information?")
					year = input(">")
					self.peek().removeInfo(year)
					break

				elif op == 4:	#remove all years
					#[DONE]?
					self.years = None
					break

				elif op == 5:	#delete country
					#[DONE]?
					deletedVal = self.pop()
					break

				else:
					self.peek().displayInfo()	#[REMOVE]debugging purpose only 
					break

			else:
				stackAux.push(self.pop())
		self.concatenate(stackAux)

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

	def displayInfo(self):				#prints country name&code, and every year with it's information
		print('\n' + self.cName + ' - ' + self.cCode)
		self.years.displayInfo(stackYears())

	def addInfo(self, year):				#same as below
		self.years.addInfo(year)

	def editInfo(self, year):				#is this really necessary?
		self.years.editInfo(year)

	def removeInfo(self, year):				#same as above
		self.years.removeInfo(year)

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

	def invert(self, stackF): 			#stackF = Final (inverted)
		if self.size() > 0:				#if stack is not empty
			stackF.push(self.pop())		#ads to the aux stack the first elem of self
			return self.invert(stackF)	#calls the function itself
		else:
			self.items = stackF.items

	def concatenate(self, stack):		#joins 'stack' to self stack
		for i in range(0, stack.size()):
			self.push(stack.pop())

	def displayInfo(self, stackAux):	#prints every year/info pair
		for i in range(0, self.size()):
			print(str(self.items[0][0]) + '\t' + str(self.items[0][1]) + '%')
			stackAux.push(self.pop())
		self.concatenate(stackAux)

	def addInfo(self, year):			#adds a pair year/info
		stackAux = stackYears()
		for i in range(0, self.size()):
			if int(year) == int(self.peek()[0]):
				print("The year selected already has information, to edit choose 'edit info' in the menu.")
				break
			elif int(year) < int(self.peek()[0]):
				print("What was the '%' of population with access to electricity in " + str(year))
				newValue = input(">")
				self.push(tuple([int(year), flaot(newValue)]))
				break
			else:
				stackAux.push(self.pop())
		self.concatenate(stackAux)

	def editInfo(self, year):			#edits the value of a year/value pair
		stackAux = stackYears()
		for i in range(0, self.size()):
			if int(year) == int(self.peek()[0]):
				print("\nNew value for the selected year? (" + str(year) + ")")
				newValue = input(">")
				self.pop()
				self.push(tuple([int(year), float(newValue)]))
				break
			else:
				stackAux.push(self.pop())
		self.concatenate(stackAux)
			
	def removeInfo(self, year):			#removes a year/value pair
		stackAux = stackYears()
		for i in range(0, self.size()):
			if int(year) == int(self.peek()[0]):
				self.pop()
				print("\nData from the year " + str(year) + " successfully removed!\n")
				break
			else:
				stackAux.push(self.pop())
		self.concatenate(stackAux)

if __name__ == '__main__':
	stack = loadCsvToArray()
	stack.invert(stackCountries())
	#stack.addCountry()
	#print(stack.peek().cName)
	#print(stack.peek().cCode)
	#print(stack.peek().years.peek())
	
	#stack.search('PRT', 2)	#edit
	#stack.search('PRT', 3)	#remove
	#stack.search('PRT', 1)	#add
	#stack.search('PRT', 0)	#just print to see info

	#print(stack.peek().cName)
	#print(stack.peek().cCode)
	#print(stack.peek().years.peek())
	#print(stack.peek().years.displayInfo(stackYears()))

	#saveStrutToCSV(stack)