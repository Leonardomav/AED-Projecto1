import csv
from AVL import AVLTreeCountry
from AVL import AVLTreeData



csv.register_dialect('AED', delimiter=';') #registers a new dialect, separated with ";", instead of the default ","

arvorePais=AVLTreeCountry()
dicioPais ={}
#arvorePais.searchYears(1960)


def load():
	startingYear=1960
	with open('dados.csv','r') as file:
		reader = csv.reader(file ,dialect = 'AED')
		for row in reader:
			years=AVLTreeData()
			for i in range(len(row)):
				if row[i] != '' and i!=0 and i!=1:
					years.insertYears(startingYear+(i-2),row[i])
			arvorePais.insertCountry(row[0],row[1],years)
	file.close()

def loadToDict():
	with open('dados.csv','r') as file:
		reader = csv.reader(file,dialect = 'AED')
		for row in reader:
			dicioPais[row[0]]=row[1]


def tagSearch(tag):
	if tag in dicioPais:
		node=arvorePais.countrySearch(dicioPais.get(tag))
		print(node)
	else:
		print("Error: Tag does not exist!")



load()
loadToDict()



def dataOfCountry(country):
	node=arvorePais.countrySearch(country)
	node.getYears().display()

def valuesOfYear(year):
	tree=arvorePais.searchYears(year)

def searchSpecific(country,year):
	node = arvorePais.countrySearch(country)
	if node.getYears().yearSearch(year) != None:
		print(node.getYears().yearSearch(year).getData())

def printAll():
	arvorePais.display()

#def getNodeRange(country,min,max)
#	node = arvorePais.countrySearch(country)
#	if node.getYears().getValues()

def editYear(country, year, newYear):
	node = arvorePais.countrySearch(country)
	if node.getYears().yearSearch(year) != None:
		node.getYears().yearSearch(year).setYear(newYear)

def editDara(country,year, newData):
	node = arvorePais.countrySearch(country)
	if node.getYears().yearSearch(year) != None:
		node.getYears().yearSearch(year).setData(newData)

def deleteCountry(country):
	arvorePais.delete(country)

def deleteYear(country, year):
	node = arvorePais.countrySearch(country)
	if node.getYears().yearSearch(year) != None:
		node.getYears().delete(year)

def addYears(country,year, data):
	node=arvorePais.countrySearch(country)
	node.insertYears(year,data)

def addCountry(country, tag, years):
	arvorePais.insertCountry(country, tag, years)

#dataOfCountry("Portugal")
#valuesOfYear(2000)
#searchSpecific("Portugal",2000)
#printAll()
