class CountryNode:
   	def __init__(self, country = None, years = None,  next = None, prev = None):
    	self.country = country
    	self.years = years
     	self.next = None
      	self.prev = None

   	def get_country(self):
      	return self.country

    def get_country_name(self):
    	return self.country[0]

    def get_country_tag(self):
    	return self.country[1]

   	def get_years(slef):
   		return self.years

   	def get_next(self):
    	return self.next

    def get_prev(self):
      	return self.prev

   	def set_country(self, country):
      	self.country = country

    def set_years(self, years)
    	self.years = years

   	def set_next(self, next):
      	self.next = next
      
   	def has_next(self):
      	return self.next!=None
   
   	def set_prev(self, prev):
      	self.prev = prev

   	def has_prev(self):
      	return self.prev != None

class YearNode:
	def __init__(self, year = None, data = None, next = None, prev = None):
      	self.year = year
      	self.data = data
      	self.next = None
    	self.prev = None

   	def get_year(self):
      	return self.year

   	def get_data(self):
      	return self.data

   	def get_next(self):
        return self.next

    def get_prev(self):
      	return self.prev

   	def set_data(self, data):
      	self.data = data

   	def set_year(self, data):
      	self.data = year

   	def set_next(self, next):
      	self.next = next
      
   	def has_next(self):
      	return self.next!=None
   
   	def set_prev(self, prev):
      	self.prev = prev
   
   	def has_prev(self):
    	return self.prev != None


class CountryList:
   	def __init__(self):
   		self.head = None
      
   	def is_empty(self):
    	return self.head == None

   	def add_country_beginning(self, country):
   		if self.get_node_country(country[1])==None:
	    	temp = CountryNode(country)
	      	if (self.head == None):
	        	self.head = self.tail = temp
	      	else:
	       		temp.set_prev(None)
	      		temp.set_next(self.head)
	       		self.head.set_prev(temp)
	        	self.head=temp

	       	return True
	    else:
	    	return False

   	def add_country_end(self, country):
   		if self.get_node_country(country[1])==None:
	        if (self.head == None):
	        	self.head = CountryNode(country)
	            self.tail=self.head
	        else:
	            current=self.head    
	            while(current.get_next() != None):
	            	current = current. get_next()
	            current.set_next(CountryNode(country, None, current))
	            self.tail = current.get_next()

	        return True
	    else:
	    	return False

    def add_years(self, years, country):
    	node = self.get_node_country(country)
    	if node != None:
    		node.set_years(years)
    		return True
    	else:
    		return False
      
   	def get_node_index(self, index):
    	currentNode = self.head
      	if currentNode == None:
        	return None

      	i=0
      	while i<index and currentNode.get_next()!= None:
        	currentNode = currentNode.get_next()
        	if currentNode == None:
            	break
        	i=i+1

    	return currentNode

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

  	def remove_country(self, country):
  		node = self.get_node_country(country)
    	if node != None:
    		node.get_prev().set_next()
    		return True
    	else:
    		return False


   	def insert_given_position(self, index, data):
    	newNode = DoubleNode(data)
      	if self.head == None or index == 0:
        	self.add_beginning(data)
      	elif index > 0:
        	temp = self.get_node(index)
        	if temp == None or temp.get_next() == None:
            	self.add_end(data)
         	else:
            	newNode.set_next(temp.get_next())
            	newNode.set_prev(temp)
            	temp.get_next().set_prev(newNode)
            	temp.set_next(newNode)
            
   	def delete_given_position(self, index):
    	temp=self.get_node(index)
      	if temp is not None:
        	print(temp)
         	temp.get_prev().set_next(temp.get_next())
         	if temp.get_next():
            	temp.get_next().set_prev(temp.get_prev())
       		temp.set_prev(None)
        	temp.set_next(None)
        	temp.set_data(None)

class nodestack