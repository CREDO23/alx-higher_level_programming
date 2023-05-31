#!/usr/bin/python3


"""module for a singly linked list in python"""


class Node:
    """"defines a node"""

    def __init__(self, data, next_node=None):
        """initializes the node"""

        self.data = data
        self.next_node = next_node

    @property
    def next_node(self):
        """returns the next node
        """

        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """set value of next node (it must be an integer)"""

        if (value is not None and not isinstance(value, Node)):
            raise TypeError('next_node must be a Node object')

        self.__next_node = value

    @property
    def data(self):
        """return the data of the node"""

        return (self.__data)

    @data.setter
    def data(self, value):
        """sets data (it must be an integer)"""

        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self.__data = value


class SinglyLinkedList:
    """defines a singly linked list class"""

    def __init__(self):
        """Initialition"""
        self.head = None

    def __str__(self):
        """print this linked list as this class"""

        linkedl = ""
        current = self.head
        while current:
            linkedl += str(current.data) + "\n"
            current = current.next_node
        return linkedl[:-1]

    def sorted_insert(self, value):
        """insert a node in a sorted way
        """
        new = Node(value)
        if not self.head:
            self.head = new
            return
        if value < self.head.data:
            new.next_node = self.head
            self.head = new
            return
        current = self.head
        while current.next_node and current.next_node.data < value:
            current = current.next_node
        if current.next_node:
            new.next_node = current.next_node
        current.next_node = new
