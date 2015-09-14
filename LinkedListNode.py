'''
Created on Sep 4, 2015

@author: shearora
'''
class LinkedListNode:
    
    def __init__(self,d):
        self.__d = d
        self.__next = None
    
    def get_data(self):
        return self.__d
    
    def set_next(self,n):
        self.__next = n
       
    def get_next(self):
        return self.__next
    
    

