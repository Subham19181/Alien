class Node:
    """
    An Object for storing a single node of a linked list.
    Models two attributes - data and the link to the next node in the list.
    """

    #data = None
    next_node = None

    def __init__(self,data=None):
        self.data = data

    def __repr__(self): #__repr__ stands for representation when we access in the console
        return f"<Node data: %s>" % self.data #Probably can be made with an f string

class LinkedList:
    """
    Singly Linked List
    """

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        """
        Returns the number of nodes in the  list
        Takes O(n) time
        """

        current = self.head #current is a Node Object
        count = 0

        while current: #means current is NOT None
            count += 1
            current = current.next_node

        return count

    def add(self, data):
        """
        Adds new Node containing data at head of the list
        Taks O(1) time
        """
        new_node = Node(data)
        new_node.next_node = self.head #first we assign the reference to the head
        self.head = new_node           #afterwards we take the new node be the head of the lst

    def search(self, key):
        """
        Searches for the first node containing data that matches the key
        Returns the node or 'None' if not found
        Takes O(n) time
        """
        current = self.head
        while current: #means current is NOT None and u have a Node Object in the Linked List
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None

    def insert(self, data, index):
        """
        Inserts a new Node containing data at index position.
        Insertion takes O(1) time but finding the node
        at the insertion point takes O(n) linear time.
        Therefore it takes overall O(N) time.
        """

        if index == 0:
            self.add(data)

        if index > 0:
            new = Node(data)
            position = index
            current = self.head

            while position > 1: #we want to be at 1 so we can make the connections in the nodes
                current = current.next_node
                position -= 1

            prev = current
            next = current.next_node
            prev.next_node = new
            new.next_node = next

    def remove(self, key):
        """
        Removes Node containing data that matches the key
        Returs the node or None if key doesnt exist
        Takes O(n) time
        """
        current = self.head
        previous = None
        found = False

        while current and not found:

            if current.data == key and current == self.head:
                found = True
                self.head = current.next_node

            elif current.data == key:
                found = True
                previous.next_node = current.next_node

            else:
                previous = current
                current = current.next_node

        return current


    def __repr__(self):
 
        nodes = []
        current = self.head

        while current: #means current is NOT None
            if current is self.head:
                nodes.append(f"[Head: {current.data}]")
            elif current.next_node is None:
                nodes.append(f"[Tail {current.data}]")
            else:
                nodes.append(f"[{current.data}]")

            current = current.next_node

        return '-> '.join(nodes)
