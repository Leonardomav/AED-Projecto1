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

	while True:
		print("Which one of the following data structure you want want to use?")
		print("1 - Dictionaries")
		print("2 - DoubleLinkedLists of DoubleLinkedLists")
		print("3 - @Sopas Strut")
		print("0 - Quit")
		structPicked= int(input("> "))
		if structPicked == 1 or structPicked == 2 or structPicked == 3:
			break
		else:
			print("Option not available... Try Again...\n")
	
	return structPicked

def menu(mont, countriesList, sopa, structPicked):

	while True:
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
		print("0 - Quit")
		choice = int(input("> "))

		#delete the "continues"
		if choice == 1:
			if structPicked == 1:
				continue
				#@SOPAS STRUT FUNCTION HERE
			elif structPicked == 2:
				leo.allYearsFromCountry(countriesList)
			elif structPicked == 3:
				continue
				#@MONTEIRO STRUT FUNCTION HERE
			break

		elif choice == 2:
			if structPicked == 1:
				continue
				#@SOPAS STRUT FUNCTION HERE
			elif structPicked == 2:
				continue
				#@LEO STRUT FUNCTION HERE
			elif structPicked == 3:
				continue
				#@MONTEIRO STRUT FUNCTION HERE
			break

		elif choice == 3:
			if structPicked == 1:
				continue
				#@SOPAS STRUT FUNCTION HERE
			elif structPicked == 2:
				continue
				#@LEO STRUT FUNCTION HERE
			elif structPicked == 3:
				continue
				#@MONTEIRO STRUT FUNCTION HERE
			break

		elif choice == 4:
			if structPicked == 1:
				continue
				#@SOPAS STRUT FUNCTION HERE
			elif structPicked == 2:
				continue
				#@LEO STRUT FUNCTION HERE
			elif structPicked == 3:
				continue
				#@MONTEIRO STRUT FUNCTION HERE
			break

		elif choice == 5:
			if structPicked == 1:
				continue
				#@SOPAS STRUT FUNCTION HERE
			elif structPicked == 2:
				continue
				#@LEO STRUT FUNCTION HERE
			elif structPicked == 3:
				continue
				#@MONTEIRO STRUT FUNCTION HERE
			break

		elif choice == 6:
			if structPicked == 1:
				continue
				#@SOPAS STRUT FUNCTION HERE
			elif structPicked == 2:
				continue
				#@LEO STRUT FUNCTION HERE
			elif structPicked == 3:
				continue
				#@MONTEIRO STRUT FUNCTION HERE
			break

		elif choice == 7:
			if structPicked == 1:
				continue
				#@SOPAS STRUT FUNCTION HERE
			elif structPicked == 2:
				continue
				#@LEO STRUT FUNCTION HERE
			elif structPicked == 3:
				continue
				#@MONTEIRO STRUT FUNCTION HERE
			break

		elif choice == 8:
			if structPicked == 1:
				continue
				#@SOPAS STRUT FUNCTION HERE
			elif structPicked == 2:
				continue
				#@LEO STRUT FUNCTION HERE
			elif structPicked == 3:
				continue
				#@MONTEIRO STRUT FUNCTION HERE
			break

		elif choice == 9:
			if structPicked == 1:
				continue
				#@SOPAS STRUT FUNCTION HERE
			elif structPicked == 2:
				continue
				#@LEO STRUT FUNCTION HERE
			elif structPicked == 3:
				continue
				#@MONTEIRO STRUT FUNCTION HERE
			break

		elif choice == 10:
			if structPicked == 1:
				continue
				#@SOPAS STRUT FUNCTION HERE
			elif structPicked == 2:
				continue
				#@LEO STRUT FUNCTION HERE
			elif structPicked == 3:
				continue
				#@MONTEIRO STRUT FUNCTION HERE
			break

		elif choice == 11:

			if structPicked == 1:
				continue
				#@SOPAS STRUT FUNCTION HERE
			elif structPicked == 2:
				continue
				#@LEO STRUT FUNCTION HERE
			elif structPicked == 3:
				continue
				#@MONTEIRO STRUT FUNCTION HERE
			break

		if choice == 0:
			return 0


		else:
			print("Option not available... Try Again...\n")




if __name__ == '__main__': 		
	main()