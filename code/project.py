import csv

csv.register_dialect('AED', delimiter=';')

def loadCsvToArray():
	with open('dados.csv','r') as file:
		reader = csv.reader(file, dialect='AED')
		aux=[]
		for row in reader:
			aux.append(row)
	print(aux)
	return

loadCsvToArray()