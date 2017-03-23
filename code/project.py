import monteiro as monteiro
import doubleLinkedLists as dll
import sopas as sopas

def loadStructures(): #loads the structures to be used in the program
	DoubleLinkedLists = dll.loadCsvToArray()
	monteiro = "Stacks" #chage this for the load
	sopas = "AVL" #chage this for the load

	return [monteiro, DoubleLinkedLists, sopas]

def main():
	countriesStack, countriesList, countriesAVL = loadStructures()

	while True:
		structPicked=menuDataStrut()
		if structPicked == 0:
			break
		menu(countriesStack, countriesList, countriesAVL, structPicked)
	

def menuDataStrut():

	while True:
		print("\nWhich one of the following data structure you want want to use?")
		print("1 - Dictionaries")
		print("2 - DoubleLinkedLists of DoubleLinkedLists")
		print("3 - @Sopas Strut")
		print("0 - Quit")
		structPicked= int(input("> "))
		if structPicked == 0 or structPicked == 1 or structPicked == 2 or structPicked == 3:
			break
		else:
			print("Option not available... Try Again...\n")
	
	return structPicked

def menu(countriesStack, countriesList, countriesAVL, structPicked):

	while True:
		print("\n---------------------------------------------------\nMENU")
		print("1  - Search all the years with available information of one country;")
		print("2  - Search all the countries information of one year;")
		print("3  - Search one year information of one country;")
		print("4  - Search all the years of all the countries;")
		print("5  - Search a range of percentages of one country;")
		print("6  - Edit year of a country;")
		print("7  - Edit year's respective percentage of a country;")
		print("8  - Remove one country;")
		print("9  - Remove one year of one country;")
		print("10 - Add one country;")
		print("11 - Add one pair [Year, Percentage] to a country;")
		print("0  - Quit")
		choice = int(input("> "))

		#delete the "continues"
		if choice == 1:
			if structPicked == 1:
				continue
				#@SOPAS STRUT FUNCTION HERE
			elif structPicked == 2:
				dll.allYearsFromCountry(countriesList)
			elif structPicked == 3:
				continue
				#@MONTEIRO STRUT FUNCTION HERE

		elif choice == 2:
			if structPicked == 1:
				continue
				#@SOPAS STRUT FUNCTION HERE
			elif structPicked == 2:
				dll.allCountryFromYear(countriesList)
			elif structPicked == 3:
				continue
				#@MONTEIRO STRUT FUNCTION HERE

		elif choice == 3:
			if structPicked == 1:
				continue
				#@SOPAS STRUT FUNCTION HERE
			elif structPicked == 2:
				dll.oneYearFromOneCoutry(countriesList)
			elif structPicked == 3:
				continue
				#@MONTEIRO STRUT FUNCTION HERE

		elif choice == 4:
			if structPicked == 1:
				continue
				#@SOPAS STRUT FUNCTION HERE
			elif structPicked == 2:
				dll.allYearsFromAllCountries(countriesList)
			elif structPicked == 3:
				continue
				#@MONTEIRO STRUT FUNCTION HERE

		elif choice == 5:
			if structPicked == 1:
				continue
				#@SOPAS STRUT FUNCTION HERE
			elif structPicked == 2:
				dll.RangeOfDataOfOneCountry(countriesList)
			elif structPicked == 3:
				continue
				#@MONTEIRO STRUT FUNCTION HERE

		elif choice == 6:
			if structPicked == 1:
				continue
				#@SOPAS STRUT FUNCTION HERE
			elif structPicked == 2:
				dll.editYearOfACountry(countriesList)
			elif structPicked == 3:
				continue
				#@MONTEIRO STRUT FUNCTION HERE

		elif choice == 7:
			if structPicked == 1:
				continue
				#@SOPAS STRUT FUNCTION HERE
			elif structPicked == 2:
				dll.editValueOfAYear(countriesList)
			elif structPicked == 3:
				continue
				#@MONTEIRO STRUT FUNCTION HERE

		elif choice == 8:
			if structPicked == 1:
				continue
				#@SOPAS STRUT FUNCTION HERE
			elif structPicked == 2:
				dll.removeCountry(countriesList)
			elif structPicked == 3:
				continue
				#@MONTEIRO STRUT FUNCTION HERE

		elif choice == 9:
			if structPicked == 1:
				continue
				#@SOPAS STRUT FUNCTION HERE
			elif structPicked == 2:
				dll.removeYearFromCountry(countriesList)
			elif structPicked == 3:
				continue
				#@MONTEIRO STRUT FUNCTION HERE

		elif choice == 10:
			if structPicked == 1:
				continue
				#@SOPAS STRUT FUNCTION HERE
			elif structPicked == 2:
				dll.addCountry(countriesList)
			elif structPicked == 3:
				continue
				#@MONTEIRO STRUT FUNCTION HERE

		elif choice == 11:

			if structPicked == 1:
				continue
				#@SOPAS STRUT FUNCTION HERE
			elif structPicked == 2:
				dll.addYearToCountry(countriesList)
			elif structPicked == 3:
				continue
				#@MONTEIRO STRUT FUNCTION HERE

		elif choice == 0:
			break

		else:
			print("Option not available... Try Again...\n")




if __name__ == '__main__': 		
	main()