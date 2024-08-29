#pop - removes the top item
#push - adds to the top of the list
#top - removes the top item from the stack
#peak - returns the top item from the stack
class ListStackError (Exception):
    pass

class Liststack:

    def __init__(self, maxSize = 10):
        self.__stack = [None] * maxSize
        self.__numOfItems = 0

    def push(self, itemToPush):
        if self.__numOfItems < len(self.__stack):
            self.__stack[self.__numOfItems] = itemToPush
            self.__numOfItems += 1
            return True
        else:
            return False
            #raise ListStackError ("Error - pushing into a full stack") 

    def peak(self):
        pass
    
    def pop(self):
        pass
            
    def top(self):
        pass
            