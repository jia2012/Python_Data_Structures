from LinkedListNode import LinkedListNode

class DoubleLinkedListNode(LinkedListNode):
    
    def __init__(self,d):
        LinkedListNode.__init__(self, d)
        self.__prev = None
    
    def set_prev(self,prev):
        self.__prev = prev
    
    def get_prev(self):
        return self.__prev
    
   
    
    