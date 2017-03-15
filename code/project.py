import csv

csv.register_dialect('AED', delimiter=';') #registers a new dialect, separated with ";", instead of the default ","

#list of lists
def loadCsvToArray():
	#loads the csv file into an array of arrays, 1
	with open('dados.csv','r') as file: 			#opens the csv file
		reader = csv.reader(file, dialect='AED')	
		array = []									#structure to save the good stuff :^)
		for row in reader:
			array.append(row)						#appends a "line" of the '.csv' file, and adds it to the list 'Array'
	
	return array 									#returns the 'Array' so you can use it later

#data structure #2




#data structure #3