import monteiro as monteiro
import leo as leo
import sopas as sopas
def loadStructures():		#loads the structures to be used in the program
	struct2 = '@leo'
	struct3 = '@sopas'
	return [monteiro.createDict(), struct2, struct3]


def menu():
	return

if __name__ == '__main__': 		
	a1, a2, a3 = loadStructures()	#a1 -> tuple with 1 dict [0] and 2 lists [1] and [2]
	a1_1 = a1[0]
	a1_2 = a1[1]
	a1_3 = a1[2]
	print(a1_2)