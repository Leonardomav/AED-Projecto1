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
			i=2
			for i in range(len(row)):
				if row[i] != '':
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
		node=arvorePais.CountrySearch(dicioPais.get(tag))
		print(node)
	else:
		print("Error: Tag does not exist!")



load()
loadToDict()
arvorePais.display()
print(arvorePais.CountrySearch("Portugal"))

#arvorePais.searchYears(1960)


def menu():
	load()
	loadToDict()
	menu=True
	while menu:
		print("1 - Search for a Country (by name) in the tree\n")
		print("2 - Search for a Country (by tag) in the tree\n")
		print("3 - Search for a Year in the tree\n")
		print("4 - Edit year\n")
		print("5 - Edit Country\n\nChoice: ")
		print("6 - Insert Country\n")
		print("7 - Delete Country\n")
		print("8 - Insert [year,value]")
		print("0 - Exit")
		choice = input()

		if choice == 1:
			string = input("Which Country are you looking for? ")
			arvorePais.CountrySearch(string)

		elif choice == 2:
			string = input("Which country's tag are you looking for? ")
			tagSearch(string)
		#elif choice == 3:
			#to be completed
		elif choice == 4:
			string = input("Which year would you like to edit? ")
			#to be completed
		elif choice == 5:
			string = input("Which country would you like to edit? ")
			node=arvorePais.CountrySearch(string)
			print("What would you like to edit?\n1 - Name\n2 - Tag\n3 - Year")
			choice2 = input("Choice: ")
			if choice2 == 1:
				string = input("Insert new name: ")
				node.country=string
			elif choice2 == 2:
				string = input("Insert new tag: ")
				node.tag = string
			#elif choice2 == 3: 
				#to be competed
		#elif choice == 0:
			#menu = False
		else:
			print("Invalid input")



