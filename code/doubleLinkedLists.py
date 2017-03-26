import time
import csv

class CountryNode:
    def __init__(self, country = None, years = None,  next = None, prev = None):
        self.country = country
        self.years = years 
        self.next = next
        self.prev = prev

    def getCountry(self):
        return self.country

    def getCountryName(self):
        return self.country[0]

    def getCountryTag(self):
        return self.country[1]

    def getYears(self):
        return self.years

    def getNext(self):
        return self.next

    def getPrev(self):
        return self.prev

    def setCountry(self, country):
        self.country = country

    def setYears(self, years):
        self.years = years

    def setNext(self, next):
        self.next = next

    def setPrev(self, prev):
        self.prev = prev

class YearNode:
    def __init__(self, year = None, data = None, next = None, prev = None):
        self.year = year
        self.data = data
        self.next = next
        self.prev = prev

    def getYear(self):
        return self.year

    def getData(self):
        return self.data

    def detData(self, data):
        self.data = data

    def setYear(self, year):
        self.year = year

    def setNext(self, next):
        self.next = next

    def getNext(self):
        return self.next

    def getPrev(self):
        return self.prev

    def setPrev(self, prev):
        self.prev = prev


class CountryList:
    def __init__(self):
        self.head = None    

    #add country to the end of the list {country -> []}
    def addCountry(self, country):

        currentNode = self.head

        if currentNode != None:
            while country[1] not in currentNode.getCountry() and country[0] not in currentNode.getCountry() and currentNode.getNext()!=None:
                currentNode = currentNode.getNext()

            if  (country[1] in currentNode.getCountry()) and (country[0] in currentNode.getCountry()):
                last = None
            else: 
                last = currentNode
        else:
            last = "Pass"


        if last != None:
            if (self.head == None):
                self.head = CountryNode(country)
                self.tail=self.head
                
            else:   
                last.setNext(CountryNode(country, None, None, currentNode))
                self.tail = last.getNext()
            return True
        
        else:
            return False

    #check if country exists, then add yearsList to that country {country -> TAG}
    def addYears(self, years, country):
        node = self.getNodeCountry(country)
        if node != None and node.getYears()==None:
            node.setYears(years)
            return True
        else:
            return False

    #Returns CountryNode, given TAG or NAME of the country
    def getNodeCountry(self, country):
        currentNode = self.head
        found = None

        if currentNode == None:
            return None

        while country not in currentNode.getCountry() and currentNode.getNext()!=None:
            currentNode = currentNode.getNext()

        if country in currentNode.getCountry():
            found = currentNode

        return found

    #remove CountryNode, given TAG or NAME of the country
    def removeCountry(self, country):
        temp=self.getNodeCountry(country)
        if temp != None:
            if temp.getPrev() == None and temp.getNext() == None:
                self.head = None
            elif temp.getPrev() == None and temp.getNext() != None:
                self.head = temp.getNext()
                temp.getNext().setPrev(None)
            elif temp.getPrev() != None and temp.getNext() == None:
                self.tail = temp.getNext()
                temp.getPrev().setNext(None)
            else:
                temp.getPrev().setNext(temp.getNext())
                temp.getNext().setPrev(temp.getPrev())            
                
            temp.setPrev(None)
            temp.setNext(None)
            temp.setCountry(None)
            temp.setYears(None)
            
            return True
        else:
            return False    

class YearsList:
    def __init__(self):
        self.head = None

    #add YearNode to the end of the list if the year does no exist {requiers year and value} 
    def addYear(self, year, value):
        current = self.head

        if current == None:
            if (self.head == None):
                self.head = YearNode(year, value)                
                self.tail=self.head
                return True

        else:

            while current.getNext() != None and current.getYear() <year:
                current = current.getNext()

            if current.getYear() != year:

                if current.getPrev() != None and current.getNext() != None:
                    newNode = YearNode(year, value, current, current.getPrev())
                    current.getPrev().setNext(newNode)
                    current.setPrev(newNode)
                    self.tail = current.getNext()
                    
                elif current.getPrev() == None and current.getNext() != None:
                    newNode = YearNode(year, value, current, None)
                    current.setPrev(newNode)
                    self.head = newNode
                    
                elif current.getPrev() != None and current.getNext() == None:
                    if current.getYear() < year:
                        newNode = YearNode(year, value, None, current)
                        current.setNext(newNode)
                        self.tail = newNode
                    else:
                        newNode = YearNode(year, value, current, current.getPrev())
                        current.getPrev().setNext(newNode)
                        current.setPrev(newNode)
                        
                else: 
                    if current.getYear() > year:
                        newNode = YearNode(year, value, current, None)
                        current.setPrev(newNode)
                        self.head=newNode
                    else:
                        newNode = YearNode(year, value, None, current)
                        current.setNext(newNode)
                        self.tail=newNode               
                
                return True

            else:
                return False

    #Returns YearNode given the year
    def getNodeYear(self, year):
        currentNode = self.head
        found = None

        if currentNode == None:
            return None

        while year > currentNode.getYear() and currentNode.getNext()!=None:
            currentNode = currentNode.getNext()

        if year == currentNode.getYear():
            found = currentNode

        return found

    #retrun list with all the year with the value in the range
    def getNodeRange(self, min = 0, max = 100):
        currentNode = self.head

        while currentNode!=None:
            if currentNode.getData() >= min and currentNode.getData() <= max:
                print('-> '  + str(currentNode.getYear()) + ' - ' + str(currentNode.getData()) + '%')

            currentNode = currentNode.getNext()

    #chages year to yearnew
    def editYear(self, yearold, yearnew):
        if self.getNodeYear(yearnew)==None:
            node = self.getNodeYear(yearold)
            if node!= None:
                value = node.getData()
                self.removeYear(yearold)
                self.addYear(yearnew, value)
                return True
            else:
                return False
        else:
            return False

    #edit value of given year to valuenew
    def editValue(self, year, valuenew):
        node = self.getNodeYear(year)
        if node!= None:
            node.detData(valuenew)
            return True
        else:
            return False

    #remove year, given the year
    def removeYear(self, year):
        temp=self.getNodeYear(year)
        if temp != None:
            if temp.getPrev() == None and temp.getNext() == None:
                self.head = None
            elif temp.getPrev() == None and temp.getNext() != None:
                self.head = temp.getNext()
                temp.getNext().setPrev(None)
            elif temp.getPrev() != None and temp.getNext() == None:
                self.tail = temp.getNext()
                temp.getPrev().setNext(None)
            else:
                temp.getPrev().setNext(temp.getNext())
                temp.getNext().setPrev(temp.getPrev())            
                
            temp.setPrev(None)
            temp.setNext(None)
            temp.detData(None)
            temp.setYear(None)
            
            return True
        else:
            return False



#------------------------------------------------------------------

csv.register_dialect('AED', delimiter=';') #registers a new dialect, separated with ";", instead of the default ","

#loads the csv file to struct
def loadCsv():
    with open('dados.csv','r') as file:             
        reader = csv.reader(file, dialect='AED')    
        countries = CountryList()
        iterator = 0
        for row in reader:
            if iterator == 0:
                iterator = 1
            else:
                years = YearsList()
    
                for i in range(2, len(row)):
                    if row[i] != '':
                        years.addYear(int(i + 1958), float(row[i]))
                        
                countries.addCountry([row[0], row[1]])
                countries.addYears(years, row[1])

    file.close()
    return countries

def inputInt(string):
    while True:
        try:
            num = int(input(string))
        except ValueError:
            print("Error... Please try again...")
            continue
        else:
            return num

def inputFloat(string):
    while True:
        try:
            num = float(input(string))
        except ValueError:
            print("Error... Please try again...")
            continue
        else:
            return num


def checkBool(check):
    if check:
        print("Done...\n")
    else:
        print("Error...\n")    

#Given the main double linked list prints an array with all the pair Country name / TAG
def printAllCountries(ListCountries):
    currentNode = ListCountries.head
    while currentNode!=None:
        print('-> ' + currentNode.getCountryName() + ' - ' + currentNode.getCountryTag())
        currentNode = currentNode.getNext()

#Used to ask the user for an input of country name / tag
def pickCountry(ListCountries):
    printAllCountries(ListCountries)
    countryPicked = input("\nWhat country do you want?\n> ")
    countryNode = ListCountries.getNodeCountry(countryPicked)
    if countryNode != None and countryNode.getYears() != None:
        return countryNode
    else:
        return None
    
#Main function to print all the years with values from a given country
def allYearsFromCountry(ListCountries):
    country=pickCountry(ListCountries)
    if country != None:
        if country.getYears() != None:
            currentNode = country.getYears().head
            print('\nYears with info or -> ' + country.getCountryName() + ' - ' + country.getCountryTag() + ':')
            while currentNode!=None:
                print(str(currentNode.getYear()) + ' - ' + str(currentNode.getData())+'%')
                
                currentNode = currentNode.getNext()
    else: 
        print("\n..Country does not exist or has no information available...\n")

    
    
#Print a pylist with the values of all countrys of a given year
def allCountryFromYear(ListCountries):
    yearPicked = inputInt("\nWhat year do you want?\n> ")
    currentNode = ListCountries.head
    while currentNode!=None:
        value = currentNode.getYears().getNodeYear(yearPicked)
        if value!=None:
            print(currentNode.getCountryName() + ' - ' + str(value.getData())+'%')
        else:
            print(currentNode.getCountryName() + ' - No Data Available')
        currentNode = currentNode.getNext()

#Prints the value of one year of one given country
def oneYearFromOneCountry(ListCountries):
    countryPicked = pickCountry(ListCountries)
    if countryPicked != None:
        if countryPicked.getYears() != None:
            yearPicked = inputInt("\nWhat year do you want?\n> ")
            yearNode = countryPicked.getYears().getNodeYear(yearPicked)
            if yearNode != None:
                print('\n' + countryPicked.getCountryName() + ' - ' + str(yearPicked) + ' - '  + str(yearNode.getData())+'%')
            else: 
                print("No Data Available\n")

    else:
        print("\n..Country does not exist or has no information available...\n")
    
#Prints all the years from all the countries
def allYearsFromAllCountries(ListCountries):
    currentNodeC = ListCountries.head
    while currentNodeC!=None:
        print('\nCountry - ' + currentNodeC.getCountryName() + ' - ' + currentNodeC.getCountryTag())
        if(currentNodeC.getYears() != None):
            currentNodeY = currentNodeC.getYears().head
            while currentNodeY!=None:
                print(str(currentNodeY.getYear()) + ' - ' + str(currentNodeY.getData())+'%') 
            
                currentNodeY = currentNodeY.getNext()
            
        else:
            print("This country as no data registred...")
        
        currentNodeC = currentNodeC.getNext()
        
#Prints the values and respective years from a certain country between a given range of percentages
def RangeOfDataOfOneCountry(ListCountries):
    country = pickCountry(ListCountries)
    if country != None:
        if country.getYears()!=None:
            Min = inputFloat("\nMinimum Percentage:\n> ")
            Max = inputFloat("Maximum Percentage:\n> ")
            print('\n' + country.getCountryName() + ' - Years with the values between ' + str(Min) + '%' +' and ' + str(Max)+'%:')
            country.getYears().getNodeRange(Min, Max)

    else:
        print("\n..Country does not exist or has no information available...\n")
        
#if it exists, edits one year of a country
def editYearOfACountry(ListCountries):
    country = pickCountry(ListCountries)
    if country != None:
        if country.getYears() != None:
            yearPicked = inputInt("\nWhat year do you want to edit?\n> ")
            newYear = inputInt("What year do you want to insert?\n> ")
            checker = country.getYears().editYear(yearPicked, newYear)
            checkBool(checker)

    else:
        print("\n..Country does not exist or has no information available...\n")
         
#if it exists, edits the value of one year of a country
def editValueOfAYear(ListCountries):
    country = pickCountry(ListCountries)
    if country != None:
        if country.getYears() != None:
            yearPicked = inputInt("\nWhat year do you want to edit?\n> ")
            newValue = inputFloat("What value do you want to insert?\n> ")
            checker = country.getYears().editValue(yearPicked, newValue)
            checkBool(checker)

    else:
        print("\n..Country does not exist or has no information available...\n")
    
#Remove completly one country
def removeCountry(ListCountries):
    printAllCountries(ListCountries)
    country = input("\nWhat country do you want to remove?\n> ")
    checker = ListCountries.removeCountry(country)
    checkBool(checker)
    
#Remove avalable info for one year of one country
def removeYearFromCountry(ListCountries):
    country = pickCountry(ListCountries)
    if country != None:
        if country.getYears() != None:
            yearPicked = inputInt("\nWhat year do you want to remove?\n> ")
            checker = country.getYears().removeYear(yearPicked)
            checkBool(checker)

    else: 
        print("\n..Country does not exist or has no information available...\n")
           
#Add a country with year->none 
def addCountry(ListCountries):
    countryName = input("\nName of the country:\n> ")
    countryTAG = input("TAG of the country:\n> ")
    country = []
    country.append(countryName)
    country.append(countryTAG)
    checker = ListCountries.addCountry(country)
    checkBool(checker) 
    
#add year to a country
def addYearToCountry(ListCountries):
    printAllCountries(ListCountries)
    countryPicked = input("\nWhat country do you want?\n> ")
    countryNode = ListCountries.getNodeCountry(countryPicked)
    year = inputInt("\nYear you want to add:\n> ")
    value = inputFloat("Percentage you want to add:\n> ")

    if countryNode == None:
        print("\n..Country does not exist or has no information available...\n")
    elif countryNode.getYears() != None:
        checker = countryNode.getYears().addYear(year, value)
        checkBool(checker)
    else:
        listYears = YearsList()
        listYears.addYear(year, value)
        checker = ListCountries.addYears(listYears, countryNode.getCountryTag())
        checkBool(checker)

#-------------------------------------------------------------------------------------

def benchmarkingAddYearsMiddle(ListCountries):
    nYears = inputInt("\nNumber of years to add:\n>")
    start = time.time()
    yearsList = ListCountries.getNodeCountry("PRT").getYears()
    for i in range(nYears):
        yearsList.addYear(i, i)
    end = time.time()
    print('[MIDLE] - Done in ' + str(end - start) + ' seconds...')
    benchmarkingSearchYears(ListCountries, yearsList, 0, nYears)


def benchmarkingAddYearsStart(ListCountries):
    nYears = inputInt("\nNumber of years to add:\n>")
    start = time.time()
    yearsList = ListCountries.getNodeCountry("PRT").getYears()
    for i in reversed(range( -nYears, 0)):
        yearsList.addYear(i, i)
    end = time.time()
    print('[BEGINNING] - Done in ' + str(end - start) + ' seconds...')
    benchmarkingSearchYears(ListCountries, yearsList, -nYears, 0)

def benchmarkingAddYearsEnd(ListCountries):
    nYears = inputInt("\nNumber of years to add:\n>")
    start = time.time()
    yearsList = ListCountries.getNodeCountry("PRT").getYears()
    for i in range(2100, 2100+nYears):
        yearsList.addYear(i, i)
    end = time.time()
    print('[END] - Done in ' + str(end - start) + ' seconds...')
    benchmarkingSearchYears(ListCountries, yearsList, 2100, 2100+nYears)

def benchmarkingSearchYears(ListCountries, yearsList, min, max):
    start = time.time()
    for i in range(min, max):
        yearsList.getNodeYear(i)

    end = time.time()
    print('[SEARCH] - Done in ' + str(end - start) + ' seconds...')
    benchmarkingRemoveYears(ListCountries, yearsList, min, max)


def benchmarkingRemoveYears(ListCountries, yearsList, min, max):
    start = time.time()
    for i in range(min, max):
        yearsList.removeYear(i)

    end = time.time()
    print('[REMOVE] - Done in ' + str(end - start) + ' seconds...')

def benchmarkingAddCountries(ListCountries):
    nCountries = inputInt("\nNumber of countries to add:\n>")
    start = time.time()
    for i in range(nCountries):
        ListCountries.addCountry([str(i), str(i)])
    end = time.time()
    print('Added all the countries in ' + str(end - start) + ' seconds...')
    benchmarkingSearchCountries(ListCountries, nCountries)

def benchmarkingSearchCountries(ListCountries, nCountries):
    start = time.time()
    for i in range(nCountries):
        ListCountries.getNodeCountry(str(i))
    end = time.time()
    print('Searched all the countries in ' + str(end - start) + ' seconds...')
    benchmarkingRemoveCountries(ListCountries, nCountries)

def benchmarkingRemoveCountries(ListCountries, nCountries):
    start = time.time()
    for i in range(nCountries):
        ListCountries.removeCountry(str(i))
    end = time.time()
    print('Removed all the coutries in ' + str(end - start) + ' seconds...')
