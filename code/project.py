import monteiro as monteiro
import leo as leo
import sopas as sopas

def loadStructures():		#loads the structures to be used in the program
	leonardo = '@leo'
	s0pas = '@sopas'
	return [monteiro.createDict(), leonardo, s0pas]		#change later to work properly

def main():
	mont, leon, sopa = loadStructures()

	#@JMSMonteiro strut needs some more "fine tuning", not necessary if functions are properly made
	

	#@Leonardomav

	#JAfonsoS0pas

	#continue coding
	menuDataStrut(mont, leon, sopa)
	return

def menuDataStrut(mont, leon, sopa):
	print("Which one of the following data structure you want want to use?")
	print
	print("1 - Dictionaries")
	print("2 - @Leo Strut")
	print("3 - @Sopas Strut")
	choice = raw_input(">")
	#[TODO] protect input ^

	if choice == '1':
		#Run Function 
		menuMont(mont)
		return
	elif choice == '2':
		#Run Function 2
		return
	elif choice == '3':
		#Run Function3
		return

def menuMont(mont):
	#@JMSMonteiro's strut needs some more "fine tuning", not 100% needed, but useful
	montDict = mont[0]		#dictionary
	montCountry = mont[1]	#country list
	montCodes = mont[2]		#country code list

	#monteiro.showAllData(montDict, montCountry, montCodes)

	print("What do you want to do with this data structure?")
	print
	print("1 - Add a new value to a year we have no info about")
	print("2 - Edit an existing value")
	print("3 - Remove an existing value from a specific year")
	print("4 - Show existing data about every country")
	print("5 - Show existing data about a specific country")
 
if __name__ == '__main__': 		
	main()