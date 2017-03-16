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
	montDict = mont[0]		#dictionary
	montCountry = mont[1]	#country list
	montCodes = mont[2]		#country code list

	#@Leonardomav

	#JAfonsoS0pas

	#continue coding

	return

def menuDataStrut():
	print("Which one of the following data structure you want want to use?")
	print
	print("1 - Dictionaries")
	print("2 - @Leo Strut")
	print("3 - @Sopas Strut")
	choice = raw_input(">")
	#[TODO] protect input ^

	if choice == 1:
		#Run Function 
		return
	elif choice == 2:
		#Run Function 2
		return
	elif choice == 3:
		#Run Function3
		return


if __name__ == '__main__': 		
	main()