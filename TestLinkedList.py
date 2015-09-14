from LinkedListNode import LinkedListNode
from SingleLinkedList import SingleLinkedList
from DoubleLinkedList import DoubleLinkedList
from DoubleLinkedListNode import DoubleLinkedListNode

def single_linked_list_test():
    s = SingleLinkedList()
    s.add_node_at_first(LinkedListNode(4))
    s.add_node_at_first(LinkedListNode(5))
    s.add_node_at_first(LinkedListNode(7))

    s.add_node_at_last(LinkedListNode(6))
    s.add_node_at_last(LinkedListNode(9))
    print("before delete")
    s.traverse()
    s.delete_node(LinkedListNode(4))
    print("after delete")
    print("first.... %s" % s.get_first().get_data())
    print("last....%s " % s.get_last().get_data())
    print("size.....%d" % s.get_size())

    s.traverse()   
    
def double_linked_list_test():
    s = DoubleLinkedList()
    s.add_node_at_first(DoubleLinkedListNode(4))
    s.add_node_at_first(DoubleLinkedListNode(5))
    s.add_node_at_first(DoubleLinkedListNode(7))

    s.add_node_at_last(DoubleLinkedListNode(6))
    s.add_node_at_last(DoubleLinkedListNode(9))
    print("before delete")
    s.traverse()
    s.delete_node(DoubleLinkedListNode(4))
    print("after delete")
    print("first.... %s" % s.get_first().get_data())
    print("last....%s " % s.get_last().get_data())
    print("size.....%d" % s.get_size())

    s.traverse()  
    print("Reverse Traversal")
    s.reverse_traversal() 

double_linked_list_test()

'''
single_linked_list_test()
'''