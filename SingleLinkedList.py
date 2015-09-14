
class SingleLinkedList:
    
    ''' class variable shared by all instances goes here'''
    
    def __init__(self):
        self.__first = None
        self.__last = None
        self.__size = 0
        
    def add_node_at_first(self,n):
        if self.__first is None:
            self.__first = n
            self.__last = n
        else:
            n.set_next(self.__first)
            self.__first = n
        self.__size+=1
    
    def add_node_at_last(self,n):      
        if self.__last is None:
            self.__last = n
            self.__first = n
        else:
            self.__last.set_next(n)
            self.__last = n  
        self.__size+=1
    
    def delete_node(self,n):
        if self.__first is None:
            print("List is empty")
        else:
            if(self.__first.get_data()==n.get_data()):
                if(self.__first.get_next() is not None):
                    node = self.__first
                    self.__first = self.__first.get_next()
                    del node
            else:
                node = self.__first
                while (node.get_next() is not None):
                    if(node.get_next().get_data() == n.get_data()):
                        next = node.get_next()
                        node.set_next(node.get_next().get_next())
                        del next
                    else:
                        node = node.get_next()
            self.__size -= 1
                   
    def traverse(self):
        node = self.__first
        while node is not None:
            print("inside while %d" % node.get_data())
            node = node.get_next()
    
    def get_last(self):
        return self.__last
    
    def get_first(self):
        return self.__first
    
    def get_size(self):
        return self.__size

