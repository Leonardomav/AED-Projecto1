import monteiro as monteiro
import leo as leo
import sopas as sopas

def loadStructures():		#loads the structures to be used in the program
	DoubleLinkedLists = leo.loadCsvToArray()
	#the rest of the loads here..
	sopas = "AVL" #chage this for the load

	return [monteiro.createDict(), DoubleLinkedLists, sopas]

def main():
	mont, countriesList, sopa = loadStructures()

	choice=menuDataStrut()

	menu(mont, countriesList, sopa, choice)
	

def menuDataStrut():
	print("Which one of the following data structure you want want to use?\n")
	print("1 - Dictionaries")
	print("2 - DoubleLinkedLists of DoubleLinkedLists")
	print("3 - @Sopas Strut")
	structPicked= int(input("> "))
	
	return 

def menu(mont, countriesList, sopa, structPicked):
	print("\n\t\t#-#-#-#-#-#MENU#-#-#-#-#-#")
	print("1  - Search all the years with available information of one country;")
	print("2  - Search all the countries information of one year;")
	print("3  - Search one year information of one country;")
	print("4  - Search all the years of all the countries;")
	print("5  - Search a range of percentages of one country;")
	print("6  - Edit year of a country;")
	print("7  - Edit year respective percentage of a country;")
	print("8  - Remove one country;")
	print("9  - Remove one year of one country;")
	print("10 - Add one country;")
	print("11 - Add one pair [Year, Percentage] to a country;")
	choice = int(input("> "))



if __name__ == '__main__': 		
	main()