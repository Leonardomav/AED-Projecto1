import csv
from operator import itemgetter 	#testing this

csv.register_dialect('AED', delimiter=';') #registers a new dialect, separated with ";", instead of the default ","

def loadCsvToArray():
	#loads the csv file into an array of arrays, 1
	with open('dados.csv','r') as file: 			#opens the csv file
		reader = csv.reader(file, dialect='AED')	
		array = []									#structure to save the good stuff :^)
		for row in reader:							#iterates the file
			array.append(row)						#appends a "line" of the '.csv' file, and adds it to the list 'Array'
	
	file.close()									#closes the file since we don't need it open anymore
	return array									#returns the 'Array' so you can use it later

def createDict():
	dictionary = {} 	#creates a new dictionary
	origin = loadCsvToArray()	#array with the file

	for i in range(1, len(origin)):		#each country
		data = []		#creates a list to put values in

		for j in range(2, len(origin[i])):	#goes through the years & values

			if origin[i][j] != '':		#if it's not blank
				data.append([int(j + 1959), origin[i][j]]) #appends [year, value] to the key's Value array

		dictionary.update({str(origin[i][1]) : data}) 		#key value = list of [date, value]

	return dictionary

def createDictNew():	#uses the 'new' keys
	dictionary = {} 	#creates a new dictionary
	origin = loadCsvToArray()	#array with the file
	countries = []
	countryCodes = []

	for i in range(1, len(origin)):		#each country
		data = []		#creates a list to put values in
		key = str(origin[i][0] + ";" + origin[i][1])
		countries.append(origin[i][0])		#country name list
		countryCodes.append(origin[i][1])	#Country codes list

		for j in range(2, len(origin[i])):	#goes through the years & values

			if origin[i][j] != '':		#if it's not blank
				data.append([int(j + 1959), origin[i][j]]) #appends [year, value] to the key's Value array

		dictionary.update({key : data}) 		#key value = list of [date, value]

	return (dictionary, countries, countryCodes)

def searchDict(dictionary, mode):
	#searches in the dictionary for the keyWord the user inputs
	keyWord = raw_input("Which country are you looking for? Insert the code (e.g. AGO for Angola or PRT for Portugal)\n\n>")
	#input ^ [TODO] protect it
	if keyWord in dictionary.keys():	#if the keyWord == one of the keys
		data = dictionary.get(keyWord)	#gets the value of the key (keyWord)
		if mode == 0:	#default, returns nothing 
			return
		
		elif mode == 1:		#returns the keyWord, for use on other functions
			return keyWord
		
		elif mode == 2:		#returns boolean, can be useful
			return True

def searchDictNew(dictionary, mode, countries, countryCodes):
	found = False
	#searches in the dictionary for the searchWord the user inputs
	searchWord = raw_input("Which country are you looking for? Insert the name or the code:\n\n>")
	#input ^ [TODO] protect it
	if searchWord in countries:	#if the searchWord == one of the keys
		index = countries.index(searchWord)
		keyWord = str(countries[index] + ";" + countryCodes[index])
		found = True

	elif searchWord in countryCodes:
		index = countryCodes.index(searchWord)
		keyWord = str(countries[index] + ";" + countryCodes[index])
		found = True

	if mode == 0 and found:	#default, returns nothing
		return
	
	elif mode == 1 and found:		#returns the keyWord, for use on other functions
		return keyWord
	
	elif mode == 2 and found:		#returns boolean, can be useful
		return True

def addValue(dictionary):
	word = searchDict(dictionary, 1) 	#keyWord -> dict key
	years = []
	values = dictionary.get(word)		#values for the keyWord
	print("\n") 						#Aesthetic purposes
	for i in range(0, len(values)):
		years.append(values[i][0])		#Creates a list with the years we have data on

	yearToAdd = raw_input("Which year do you want to add info about?\n\n>")
	#[TODO] protect input ^

	if int(yearToAdd) in years:			#self explanatory IMO
		print("Year already in the directory, if you want to edit it, select the 'edit' option")

	else:
		valueToAdd = raw_input("What's the value you want to add?\n\n>")		#[TODO]edit this
		#[TODO] protect input ^
		values.append([int(yearToAdd), valueToAdd])		#adds the new information to the values list
		values = sorted(values, key = itemgetter(0))	#sorts the list of years/values
		dictionary.update({word : values})			#updates the dictionary

def editValue(dictionary):
	word = searchDict(dictionary, 1) 	#keyWord -> dict key
	years = []
	values = dictionary.get(word)		#values for the keyWord
	print("\n") 						#Aesthetic purposes
	for i in range(0, len(values)):
		printYearvalue(values[i])		#Prints existing data format: "Year - Value"
		years.append(values[i][0])		#Creates a list with the years we have data on

	valueToEdit = raw_input("Which year you want to edit?\n\n>")
	#[TODO] protect input ^

	for i in range(0, len(values)):
		if int(valueToEdit) == values[i][0]:		#needs to have the int() in order to work
			newValue = raw_input("What should be the new value?")	#asks for the new value
			#[TODO] protect input ^
			values[i][1] = newValue					#changes the value
			dictionary.update({word : values})		#updates the dictionary
			break									#stops the iteration, no need to continue (obvious, right?)

def removeValue(dictionary):
	word = searchDict(dictionary, 1) 	#keyWord -> dict key
	years = []
	values = dictionary.get(word)		#values for the keyWord
	print("\n") 						#Aesthetic purposes
	for i in range(0, len(values)):
		printYearvalue(values[i])		#Prints existing data format: "Year - Value"
		years.append(values[i][0])		#Creates a list with the years we have data on

	valueToRemove = raw_input("Which year you want to remove?\n\n>")
	#[TODO] protect input ^

	for i in range(0, len(values)):
		if int(valueToRemove) == values[i][0]:		#needs to have the int() in order to work
			values.pop(i)							#removes the specified year from the list
			dictionary.update({word : values})		#updates the dictionary
			break									#stops the iteration, no need to continue (obvious, right?)

def printYearvalue(values):		#self explanatory, I think
	print(str(values[0]) + " - " + values[1])	#"Year - Value"

#Rembemer to remove this lines under
if __name__ == '__main__':
	dictionary = createDict()
	dictionaryNew, countries, countryCodes = createDictNew()
	searchDictNew(dictionaryNew, 1, countries, countryCodes)
	#searchDict(dictionary)
	#removeValue(dictionary)