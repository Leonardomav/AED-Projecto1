#@source: https://github.com/recluze/python-avl-tree/blob/master/simple_avl.py

outputdebug = False 

def debug(msg):
    if outputdebug:
        print (msg)


class countryNode():
    def __init__(self, country, tag, years):
        self.country = country
        self.tag = tag
        self.years = years
        self.left = None 
        self.right = None 


    def getCountry(self):
        return self.country

    def getTag(self):
        return tag.self

    def getYears(self):
        return self.years

    def setYears(self,years):
        self.years=years

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right



#-------------------------------------------------------------------------------------XXXXXXXX----------------------------------------------------------------------------------------------------------------#
class yearNode:
    def __init__(self, year = None, data = None):
        self.year = year
        self.data = data
        self.left = None
        self.right = None

    def getYear(self):
        return self.year

    def getData(self):
        return self.data

    def getRight(self):
        return self.right

    def getLeft(self):
        return self.left

    def setData(self, data):
        self.data = data

    def setYear(self, year):
        self.year=year



class AVLTreeData():
    def __init__(self, *args):
        self.node = None 
        self.height = -1  
        self.balance = 0; 
        
        if len(args) == 1: 
            for i in args[0]: 
                self.insert(i)
                
    def height(self):
        if self.node: 
            return self.node.height 
        else: 
            return 0 
    
    def is_leaf(self):
        return (self.height == 0)

    def display(self, level=0, pref=''):
        '''
        Display the whole tree. Uses recursive def.
        TODO: create a better display using breadth-first search
        '''
        self.update_heights()  # Must update heights before balances
        self.update_balances()
        if(self.node != None):
            print ('-' * level * 2, pref, self.node.getYear(),",",self.node.getData())
            if self.node.left != None:
                self.node.left.display(level + 1, '<')
            if self.node.left != None:
                self.node.right.display(level + 1, '>')



    def insertYears(self, year, data):
        tree = self.node
        
        newnode = yearNode(year, data)
        
        if tree == None:
            self.node = newnode 
            self.node.left = AVLTreeData() 
            self.node.right = AVLTreeData()
            debug("Inserted key [" + str(year) + "]")
        
        elif year < tree.year: 
            self.node.left.insertYear(year, data)
            
        elif year > tree.year: 
            self.node.right.insertYears(year, data)
        
        else: 
            debug("Key [" + str(year) + "] already in tree.")
            
        self.rebalance()

    def yearSearch(self,year):
        tree=self.node
        if tree:
            if tree.getYear() == year:
                return tree

            elif year < tree.getYear():
                return self.node.left.yearSearch(year)

            elif year > tree.getYear():
                return self.node.right.yearSearch(year)

        
    def rebalance(self):
        ''' 
        Rebalance a particular (sub)tree
        ''' 
        # key inserted. Let's check if we're balanced
        self.update_heights(False)
        self.update_balances(False)
        while self.balance < -1 or self.balance > 1: 
            if self.balance > 1:
                if self.node.left.balance < 0:  
                    self.node.left.lrotate() # we're in case II
                    self.update_heights()
                    self.update_balances()
                self.rrotate()
                self.update_heights()
                self.update_balances()
                
            if self.balance < -1:
                if self.node.right.balance > 0:  
                    self.node.right.rrotate() # we're in case III
                    self.update_heights()
                    self.update_balances()
                self.lrotate()
                self.update_heights()
                self.update_balances()


            
    def rrotate(self):
        # Rotate left pivoting on self
        debug ('Rotating ' + str(self.node.year) + ' right') 
        A = self.node 
        B = self.node.left.node 
        T = B.right.node 
        
        self.node = B 
        B.right.node = A 
        A.left.node = T 

    
    def lrotate(self):
        # Rotate left pivoting on self
        debug ('Rotating ' + str(self.node.year) + ' left') 
        A = self.node 
        B = self.node.right.node 
        T = B.left.node 
        
        self.node = B 
        B.left.node = A 
        A.right.node = T 
        
            
    def update_heights(self, recurse=True):
        if not self.node == None: 
            if recurse: 
                if self.node.left != None: 
                    self.node.left.update_heights()
                if self.node.right != None:
                    self.node.right.update_heights()
            
            self.height = max(self.node.left.height,
                              self.node.right.height) + 1 
        else: 
            self.height = -1 
            
    def update_balances(self, recurse=True):
        if not self.node == None: 
            if recurse: 
                if self.node.left != None: 
                    self.node.left.update_balances()
                if self.node.right != None:
                    self.node.right.update_balances()

            self.balance = self.node.left.height - self.node.right.height 
        else: 
            self.balance = 0 

    def delete(self, year):
        # debug("Trying to delete at node: " + str(self.node.key))
        if self.node != None: 
            if self.node.year == year: 
                debug("Deleting ... " + str(year))  
                if self.node.left.node == None and self.node.right.node == None:
                    self.node = None # leaves can be killed at will 
                # if only one subtree, take that 
                elif self.node.left.node == None: 
                    self.node = self.node.right.node
                elif self.node.right.node == None: 
                    self.node = self.node.left.node
                
                # worst-case: both children present. Find logical successor
                else:  
                    replacement = self.logical_successor(self.node)
                    if replacement != None: # sanity check 
                        debug("Found replacement for " + str(year) + " -> " + str(replacement.year))  
                        self.node.year = replacement.year 
                        
                        # replaced. Now delete the key from right child 
                        self.node.right.delete(replacement.key)
                    
                self.rebalance()
                return  
            elif year < self.node.year: 
                self.node.left.delete(year)  
            elif year > self.node.year: 
                self.node.year.delete(year)
                        
            self.rebalance()
        else: 
            return 

    def logical_predecessor(self, node):
        ''' 
        Find the biggest valued node in LEFT child
        ''' 
        node = node.left.node 
        if node != None: 
            while node.right != None:
                if node.right.node == None: 
                    return node 
                else: 
                    node = node.right.node  
        return node 
    
    def logical_successor(self, node):
        ''' 
        Find the smallese valued node in RIGHT child
        ''' 
        node = node.right.node  
        if node != None: # just a sanity check  
            
            while node.left != None:
                debug("LS: traversing: " + str(node.year))
                if node.left.node == None: 
                    return node 
                else: 
                    node = node.left.node  
        return node 

    def check_balanced(self):
        if self == None or self.node == None: 
            return True
        
        # We always need to make sure we are balanced 
        self.update_heights()
        self.update_balances()
        return ((abs(self.balance) < 2) and self.node.left.check_balanced() and self.node.right.check_balanced())  
        
    def inorder_traverse(self):
        if self.node == None:
            return [] 
        
        inlist = [] 
        l = self.node.left.inorder_traverse()
        for i in l: 
            inlist.append(i) 

        inlist.append(self.node.year)

        l = self.node.right.inorder_traverse()
        for i in l: 
            inlist.append(i) 
    
        return inlist 


class AVLTreeCountry():
    def __init__(self, *args):
        self.node = None 
        self.height = -1  
        self.balance = 0; 
        
        if len(args) == 1: 
            for i in args[0]: 
                self.insert(i)
                
    def height(self):
        if self.node: 
            return self.node.height 
        else: 
            return 0 

    def is_leaf(self):
        self.height=0
        return (self.height) 


    def insertCountry(self, country, tag, years):
        tree = self.node
        
        newnode = countryNode(country, tag, years)
        
        if tree == None:
            self.node = newnode 
            self.node.left = AVLTreeCountry() 
            self.node.right = AVLTreeCountry()
            debug("Inserted key [" + str(country) + "]")
        
        elif country < tree.getCountry():
            self.node.left.insertCountry(country, tag, years)
            
        elif country > tree.getCountry():
            self.node.right.insertCountry(country, tag, years)
        
        else: 
            debug("Key [" + str(country) + "] already in tree.")
            
        self.rebalance()


    def display(self, level=0, pref=''):
        '''
        Display the whole tree. Uses recursive def.
        TODO: create a better display using breadth-first search
        '''        
        self.update_heights()  # Must update heights before balances 
        self.update_balances()
        if(self.node != None): 
            print ('-' * level * 2, pref, self.node.getCountry(),self.node.getYears().display(), "[" + str(self.height) + ":" + str(self.balance) + "]", 'L' if self.is_leaf() else ' ')
            if self.node.left != None: 
                self.node.left.display(level + 1, '<')
            if self.node.left != None:
                self.node.right.display(level + 1, '>')
                

    def countrySearch(self,country):
        tree = self.node

        if tree.getCountry() == country:
            return tree
        
        elif country < tree.getCountry():
            return self.node.left.countrySearch(country)
            
        elif country > tree.getCountry():
            return self.node.right.countrySearch(country)


    def searchYears(self,year):
        tree = self.node
        if self.node!=None:
            if tree.getYears().yearSearch(year):
                print(tree.getCountry(),";",tree.getYears().yearSearch(year).getData())
            if self.node.getLeft() != None:
                tree.getLeft().searchYears(year)
            if self.node.getRight() != None:
                tree.getRight().searchYears(year)

    def rebalance(self):
        ''' 
        Rebalance a particular (sub)tree
        ''' 
        # key inserted. Let's check if we're balanced
        self.update_heights(False)
        self.update_balances(False)
        while self.balance < -1 or self.balance > 1: 
            if self.balance > 1:
                if self.node.left.balance < 0:  
                    self.node.left.lrotate() # we're in case II
                    self.update_heights()
                    self.update_balances()
                self.rrotate()
                self.update_heights()
                self.update_balances()
                
            if self.balance < -1:
                if self.node.right.balance > 0:  
                    self.node.right.rrotate() # we're in case III
                    self.update_heights()
                    self.update_balances()
                self.lrotate()
                self.update_heights()
                self.update_balances()


            
    def rrotate(self):
        # Rotate left pivoting on self
        debug ('Rotating ' + str(self.node.country) + ' right') 
        A = self.node 
        B = self.node.left.node 
        T = B.right.node 
        
        self.node = B 
        B.right.node = A 
        A.left.node = T 


    def lrotate(self):
        # Rotate left pivoting on self
        debug ('Rotating ' + str(self.node.country) + ' left') 
        A = self.node 
        B = self.node.right.node 
        T = B.left.node 
        
        self.node = B 
        B.left.node = A 
        A.right.node = T 
        
            
    def update_heights(self, recurse=True):
        if not self.node == None: 
            if recurse: 
                if self.node.left != None: 
                    self.node.left.update_heights()
                if self.node.right != None:
                    self.node.right.update_heights()
            
            self.height = max(self.node.left.height,
                              self.node.right.height) + 1 
        else: 
            self.height = -1 
            
    def update_balances(self, recurse=True):
        if not self.node == None: 
            if recurse: 
                if self.node.left != None: 
                    self.node.left.update_balances()
                if self.node.right != None:
                    self.node.right.update_balances()

            self.balance = self.node.left.height - self.node.right.height 
        else: 
            self.balance = 0 

    def delete(self, country):
        # debug("Trying to delete at node: " + str(self.node.key))
        if self.node != None: 
            if self.node.country == country: 
                debug("Deleting ... " + str(country))  
                if self.node.left.node == None and self.node.right.node == None:
                    self.node = None # leaves can be killed at will 
                # if only one subtree, take that 
                elif self.node.left.node == None: 
                    self.node = self.node.right.node
                elif self.node.right.node == None: 
                    self.node = self.node.left.node
                
                # worst-case: both children present. Find logical successor
                else:  
                    replacement = self.logical_successor(self.node)
                    if replacement != None: # sanity check 
                        debug("Found replacement for " + str(country) + " -> " + str(replacement.country))  
                        self.node.country = replacement.country 
                        
                        # replaced. Now delete the key from right child 
                        self.node.right.delete(replacement.country)
                    
                self.rebalance()
                return  
            elif country < self.node.country: 
                self.node.left.delete(country)  
            elif country > self.node.coutry: 
                self.node.right.delete(country)
                        
            self.rebalance()
        else: 
            return 

    def logical_predecessor(self, node):
        ''' 
        Find the biggest valued node in LEFT child
        ''' 
        node = node.left.node 
        if node != None: 
            while node.right != None:
                if node.right.node == None: 
                    return node 
                else: 
                    node = node.right.node  
        return node 

    def logical_successor(self, node):
        ''' 
        Find the smallese valued node in RIGHT child
        ''' 
        node = node.right.node  
        if node != None: # just a sanity check  
            
            while node.left != None:
                debug("LS: traversing: " + str(node.country))
                if node.left.node == None: 
                    return node 
                else: 
                    node = node.left.node  
        return node 

    def check_balanced(self):
        if self == None or self.node == None: 
            return True
        
        # We always need to make sure we are balanced 
        self.update_heights()
        self.update_balances()
        return ((abs(self.balance) < 2) and self.node.left.check_balanced() and self.node.right.check_balanced())  
        
    def inorder_traverse(self):
        if self.node == None:
            return [] 
        
        inlist = [] 
        l = self.node.left.inorder_traverse()
        for i in l: 
            inlist.append(i) 

        inlist.append(self.node.country)

        l = self.node.right.inorder_traverse()
        for i in l: 
            inlist.append(i) 

        return inlist 

                
