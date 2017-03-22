import csv

class CountryNode:
    def __init__(self, country = None, years = None,  next = None, prev = None):
        self.country = country
        self.years = years 
        self.next = next
        self.prev = prev

    def get_country(self):
        return self.country

    def get_country_name(self):
        return self.country[0]

    def get_country_tag(self):
        return self.country[1]

    def get_years(self):
        return self.years

    def get_next(self):
        return self.next

    def get_prev(self):
        return self.prev

    def set_country(self, country):
        self.country = country

    def set_years(self, years):
        self.years = years

    def set_next(self, next):
        self.next = next

    def set_prev(self, prev):
        self.prev = prev

class YearNode:
    def __init__(self, year = None, data = None, next = None, prev = None):
        self.year = year
        self.data = data
        self.next = next
        self.prev = prev

    def get_year(self):
        return self.year

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def set_year(self, year):
        self.year = year

    def set_next(self, next):
        self.next = next

    def get_next(self):
        return self.next

    def get_prev(self):
        return self.prev

    def set_prev(self, prev):
        self.prev = prev


class CountryList:
    def __init__(self):
        self.head = None

    #check if empty
    def is_empty(self):
        return self.head == None    

    #add country to the end of the list {country -> []}
    def add_country(self, country):
        if self.get_node_country(country[1])==None and self.get_node_country(country[0])==None:
            if (self.head == None):
                self.head = CountryNode(country)
                self.tail=self.head
                
            else:
                current=self.head    
            
                while(current.get_next() != None):
                    current = current. get_next()
                    
                current.set_next(CountryNode(country, None, None, current))
                self.tail = current.get_next()
            return True
        else:
            return False

    #check if country exists, then add yearslist to that country {country -> TAG}
    def add_years(self, years, country):
        node = self.get_node_country(country)
        if node != None and node.get_years()==None:
            node.set_years(years)
            return True
        else:
            return False

    #Returns CountryNode, given the index the node
    def get_node_index(self, index):
        currentNode = self.head
        if currentNode == None:
            return None

        i=0
        while i<index:
            currentNode = currentNode.get_next()
            if currentNode == None:
                break
            i=i+1

        return currentNode

    #Returns CountryNode, given TAG or NAME of the country
    def get_node_country(self, country):
        currentNode = self.head
        found = None

        if currentNode == None:
            return None

        while country not in currentNode.get_country() and currentNode.get_next()!=None:
            currentNode = currentNode.get_next()

        if country in currentNode.get_country():
            found = currentNode

        return found

    #remove CountryNode, given TAG or NAME of the country
    def remove_country(self, country):
        temp=self.get_node_country(country)
        if temp != None:
            if temp.get_prev() == None and temp.get_next() == None:
                print("case 1")
                self.head = None
            elif temp.get_prev() == None and temp.get_next() != None:
                print("case 2")
                self.head = temp.get_next()
                temp.get_next().set_prev(None)
            elif temp.get_prev() != None and temp.get_next() == None:
                print("case 3")
                self.tail = temp.get_next()
                temp.get_prev().set_next(None)
            else:
                print("case 4")
                temp.get_prev().set_next(temp.get_next())
                temp.get_next().set_prev(temp.get_prev())            
                
            temp.set_prev(None)
            temp.set_next(None)
            temp.set_country(None)
            temp.set_years(None)
            
            return True
        else:
            return False    

class YearsList:
    def __init__(self):
        self.head = None

    #check if empty
    def is_empty(self):
        return self.head == None

    #add YearNode to the end of the list if the year does no exist {requiers year and value} 
    def add_year(self, year, value):
        if self.get_node_year(year)==None:
            if (self.head == None):
                self.head = YearNode(year, value)
                self.tail=self.head
            else:
                current=self.head    
                while(current.get_next() != None):
                    current = current.get_next()
                current.set_next(YearNode(year, value, None, current))
                self.tail = current.get_next()

            return True
        else:
            return False

    #Returns Year and Value, given the index of the node
    def get_node_index(self, index):
        currentNode = self.head
        if currentNode == None:
            return None
    
        i=0
        while i<index:
            currentNode = currentNode.get_next()
            if currentNode == None:
                break
            i=i+1
    
        return currentNode

    #Returns YearNode given the year
    def get_node_year(self, year):
        currentNode = self.head
        found = None

        if currentNode == None:
            return None

        while year != currentNode.get_year() and currentNode.get_next()!=None:
            currentNode = currentNode.get_next()

        if year == currentNode.get_year():
            found = currentNode

        return found

    #retrun list with all the year with the value in the range
    def get_node_range(self, min = 0, max = 100):
        currentNode = self.head
        nodelist=[]

        while currentNode!=None:
            if currentNode.get_data() >= min and currentNode.get_data() <= max:
                laux=[]
                laux.append(currentNode.get_year())
                laux.append(currentNode.get_data())
                nodelist.append(laux)
            currentNode = currentNode.get_next()

        return nodelist

    #chages year to yearnew
    def edit_year(self, yearold, yearnew):
        if self.get_node_year(yearnew)==None:
            node = self.get_node_year(yearold)
            if node!= None:
                node.set_year(yearnew)
                return True
            else:
                return False
        else:
            return False

    #edit value of given year to valuenew
    def edit_value(self, year, valuenew):
        node = self.get_node_year(year)
        if node!= None:
            node.set_data(valuenew)
            return True
        else:
            return False

    #remove year, given the year
    def remove_year(self, year):
        temp=self.get_node_year(year)
        if temp != None:
            if temp.get_prev() == None and temp.get_next() == None:
                self.head = None
            elif temp.get_prev() == None and temp.get_next() != None:
                self.head = temp.get_next()
                temp.get_next().set_prev(None)
            elif temp.get_prev() != None and temp.get_next() == None:
                self.tail = temp.get_next()
                temp.get_prev().set_next(None)
            else:
                temp.get_prev().set_next(temp.get_next())
                temp.YearsListget_next().set_prev(temp.get_prev())            
                
            temp.set_prev(None)
            temp.set_next(None)
            temp.set_data(None)
            temp.set_year(None)
            
            return True
        else:
            return False



#------------------------------------------------------------------

csv.register_dialect('AED', delimiter=';') #registers a new dialect, separated with ";", instead of the default ","

#loads the csv file to @Leo struct
def loadCsvToArray():
    #loads the csv file into an array of arrays, 1
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
                        years.add_year(int(i + 1958), float(row[i]))
                        
                countries.add_country([row[0], row[1]])
                countries.add_years(years, row[1])

    file.close()
    return countries

def checkBool(check):
    if check:
        print("Done...\n")
    else:
        print("Error...\n")    

#Given the main double linked list prints an array with all the pair Country name / TAG
def printAllCountries(ListCountries):
    l=[]
    currentNode = ListCountries.head
    while currentNode!=None:
        l.append(currentNode.get_country())
        currentNode = currentNode.get_next()
    print(l)

#Used to ask the user for an input of country name / tag
def pickCountry(ListCountries):
    printAllCountries(ListCountries)
    countryPicked = input("What country do you want?\n> ") #" "
    countryNode = ListCountries.get_node_country(countryPicked)
    if countryNode != None and countryNode.get_years() != None:
        return countryNode.get_years()
    else:
        print("Country does not exist or has no information available...\n")
        return None
    
#Main function to print all the years with values from a given country
def allYearsFromCountry(ListCountries):
    country=pickCountry(ListCountries)
    if country != None:
        l=[]
        currentNode = country.head
        while currentNode!=None:
            laux=[]
            laux.append(currentNode.get_year())
            laux.append(currentNode.get_data())
            l.append(laux)    
            
            currentNode = currentNode.get_next()
    
        print(l)
    
#Print a pylist with the values of all countrys of a given year
def allCountryFromYear(ListCountries):
    yearPicked = input("What year do you want?\n> ")
    l=[]
    currentNode = ListCountries.head
    while currentNode!=None:
        laux=[]
        value = currentNode.get_years().get_node_year(yearPicked)
        laux.append(currentNode.get_country_name())
        if value!=None:
            laux.append(value.get_data())
        else:
            laux.append("No Data Available")
        l.append(laux)
        currentNode = currentNode.get_next()
    print(l)

#Prints the value of one year of one given country
def oneYearFromOneCoutry(ListCountries):
    countryPicked = pickCountry(ListCountries)
    if countryPicked != None:
        yearPicked = input("What year do you want?\n> ")
        yearNode = countryPicked.get_node_year(yearPicked)
        if yearNode != None:
            print(countryPicked.get_node_year(yearPicked).get_data())
        else: 
            print("No Data Available\n")
    
#Prints all the years from all the countries
def allYearsFromAllCountries(ListCountries):
    currentNodeC = ListCountries.head
    while currentNodeYearsListC!=None:
        l=[]
        currentNodeY = currentNodeC.get_years().head
        l.append(currentNodeC.get_country())
        while currentNodeY!=None:
            laux=[]
            laux.append(currentNodeY.get_year())
            laux.append(currentNodeY.get_data())
            l.append(laux)    
        
            currentNodeY = currentNodeY.get_next()
            
        print(l)
        currentNodeC = currentNodeC.get_next()
        
#Prints the values and respective years from a certain country between a given range of percentages
def RangeOfDataOfOneCountry(ListCountries):
    Country = pickCountry(ListCountries)
    if Country!=None:
        Min = input("Minimum Percentage:\n> ")
        Max = input("Maximum Percentage:\n> ")
        print(Country.get_node_range(Min, Max))
        
#if it exists, edits one year of a country
def editYearOfACountry(ListCountries):
    Country = pickCountry(ListCountries)
    if Country != None:
        yearPicked = input("What year do you want to edit?\n> ")
        newYear = input("What year do you want to insert?\n> ")
        checker = Country.edit_year(yearPicked, newYear)
        checkBool(checker)
         
#if it exists, edits the value of one year of a country
def editValueOfAYear(ListCountries):
    Country = pickCountry(ListCountries)
    if Country != None:
        yearPicked = input("What year do you want to edit?\n> ")
        newValue = input("What value do you want to insert?\n> ")
        checker = Country.edit_value(yearPicked, newValue)
        checkBool(checker)
    
#Remove completly one country
def removeCountry(ListCountries):
    printAllCountries(ListCountries)
    Country = input("What country do you want to remove?\n> ")
    checker = ListCountries.remove_country(Country)
    checkBool(checker)
    
#Remove avalable info for one year of one country
def removeYearFromCountry(ListCountries):
    country = pickCountry(ListCountries)
    if country != None:
        yearPicked = input("What year do you want to remove?\n> ")
        checker = country.remove_year(yearPicked)
        checkBool(checker)
            
def addCountry(ListCountries):
    countryName = input("Name of the country:\n> ")
    countryTAG = input("TAG of the country:\n> ")
    country = []
    country.append(countryName)
    country.append(countryTAG)
    checker = ListCountries.add_country(country)
    checkBool(checker) 
    
def addYearToCountry(ListCountries):
    countryName = input("Name or TAG of the country:\n> ")
    year = input("Year you want to add:\n> ")
    value = input("Percentage you want to add:\n> ")
    countryNode = ListCountries.get_node_country(countryName)
    if countryNode.get_years() != None:
        checker = countryNode.get_years().add_year(year, value)
        checkBool(checker)
    elif countryNode != None:
        listYears = YearsList()
        listYears.add_year(year, value)
        checker = ListCountries.add_years(listYears, countryNode.get_country_tag())
        checkBool(checker)
    else:
        print("Country does not exist...\n")
    

ListCountries = loadCsvToArray();
#allYearsFromCountry(ListCountries)
#allCountryFromYear(ListCountries)
#oneYearFromOneCoutry(ListCountries)
#allYearsFromAllCountries(ListCountries)
#RangeOfDataOfOneCountry(ListCountries)
#editYearOfACountry(ListCountries)
#removeCountry(ListCountries)
#removeYearFromCountry(ListCountries)
#addCountry(ListCountries)


#addYearToCountry(ListCountries)
#allYearsFromCountry(ListCountries)
addCountry(ListCountries)
allYearsFromCountry(ListCountries)
addYearToCountry(ListCountries)
allYearsFromCountry(ListCountries)
removeYearFromCountry(ListCountries)
allYearsFromCountry(ListCountries)





