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

    #add country do the end of the list {country -> []}
    def add_country(self, country):
        if self.get_node_country(country[1])==None:
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
                nodelist.append(currentNode.get_year())
            currentNode = currentNode.get_next()

        return nodelist

    #chages year to yearnew
    def edit_year(self, yearold, yearnew):
        node = self.get_node_year(yearold)
        if node!= None:
            node.set_year(yearnew)
            return True
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
                temp.get_next().set_prev(temp.get_prev())            
                
            temp.set_prev(None)
            temp.set_next(None)
            temp.set_data(None)
            temp.set_year(None)
            
            return True
        else:
            return False



#------------------------------------------------------------------

