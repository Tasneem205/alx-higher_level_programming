#!/usr/bin/python3

"""Singly linked list"""


class Node:
    """Class tp represent nodes"""
    def __init__(self, data, next_node=None):
        """init function to define a node"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """getter & setter of data"""
        return (self.__data)

    @data.setter
    def data(self, value):
        """setter of data"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.data = value

    @property
    def next_node(self):
        """getter of next node value"""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """setter of next_node value"""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """singly linked list class in python"""
    def __init__(self):
        """init function to define a SLL"""
        self.__head = None

    def sorted_insert(self, value):
        """sorted insertion function to insert in a sorted manner"""
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not not None and
                   tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """str representation of a SLL"""
        vals = []
        tmp = self.__head
        while tmp is not None:
            vals.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(vals))
