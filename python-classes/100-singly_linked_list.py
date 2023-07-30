#!/usr/bin/python3
'''
Defines a new class called Node
'''


class Node:
    """
    Class representing a node in a singly linked list.
    """
    def __init__(self, data, next_node=None):
        """
        Initialize a new Node.

        Args:
            data (int):
            The data to be stored in the node.
            next_node (Node, optional):
            The next node in the linked list. Defaults to None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Get the data stored in the node.

        Returns:
            int: The data stored in the node.
        """
        return self._data

    @data.setter
    def data(self, value):
        """
        Set the data for the node.

        Args:
            value (int): The data to be set.

        Raises:
            TypeError: If the data is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self._data = value

    @property
    def next_node(self):
        """
        Get the next node in the linked list.

        Returns:
            Node: The next node.
        """
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        """
        Set the next node in the linked list.

        Args:
            value (Node): The next node to be set.

        Raises:
            TypeError: If the next_node is not None or a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self._next_node = value


class SinglyLinkedList:
    """
    Class representing a singly linked list.
    """
    def __init__(self):
        """
        Initialize an empty singly linked list with no head node.
        """
        self.head = None

    def sorted_insert(self, value):
        """
        Insert a new node into the correct sorted
        position in the list (increasing order).

        Args:
            value (int): The value to be stored in the new node.
        """
        new_node = Node(value)
        if self.head is None or self.head.data >= value:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        Return a string representation of the linked list.

        Returns:
            str: The linked list as a string with one node number per line.
        """
        current = self.head
        nodes = []
        while current:
            nodes.append(str(current.data))
            current = current.next_node
        return '\n'.join(nodes)
