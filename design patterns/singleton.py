class Borg:
    
    """The Borg design pattern"""
    
    _shared_data = {} #Attribute dictionary

    def __init__(self):
        self.__dict__ = self._shared_data #Make an attibute dictionary
        

class Singleton(Borg): 
    
    """The singleton class"""
    def __init__(self, **kwargs):
        Borg.__init__(self)
        self._shared_data.update(kwargs) #update the attribute dictionary

    def __str__(self):
        return str(self._shared_data) #Returns the attribute dictionary for printing


#Let's create a singleton object and add our first aacronym
x = Singleton(HTTP= "Hyper Text Transfer Protocol")

#Print the object
print(x)
#Lets create another singleton object and 
#if it refers to the same attribute dictionary
#by adding another acronyms
y = Singleton(SNMP = "Simple Network Management Protocol")

#print the object
print(y)