import csv

csv.register_dialect('AED', delimiter=';') #registers a new dialect, separated with ";", instead of the default ","

#list of lists
def loadCsvToArray():
	#loads the csv file into an array of arrays, 1
	with open('dados.csv','r') as file: 			#opens the csv file
		reader = csv.reader(file, dialect='AED')	
		array = []									#structure to save the good stuff :^)
		for row in reader:							#iterates the file
			array.append(row)						#appends a "line" of the '.csv' file, and adds it to the list 'Array'
	
	file.close()									#closes the file since we don't need it open anymore
	return array									#returns the 'Array' so you can use it later

#data structure #1 - dictionary

def createDict():
	dictionary = {} 	#creates a new dictionary
	origin = loadCsvToArray()	#array with the file

	for i in range(1, len(origin)):		#each country
		data = []		#creates a list to put values in

		for j in range(2, len(origin[i])):	#goes through the years & values

			if origin[i][j] != '':		#if it's not blank
				data.append([int(j + 1959), origin[i][j]]) #appends [year, value] to the key's Value array

		dictionary.update({str(origin[i][1]) : data}) 		#key value = list of [date, value]

	#testing
	#print(dictionary.keys())

createDict()


#data structure #2





#data structure #3