# Python3 program to show inserting a node
# after a given node in given Linked List

# Node class


class Node:

    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null


# Linked List class contains a Node object
class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def push(self, new_data):

        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # This function is in LinkedList class. Inserts a
    # new node after the given prev_node. This method is
    # defined inside LinkedList class shown above */

    def insertAfter(self, prev_node, new_data):

        # 1. check if the given prev_node exists
        if prev_node is None:
            print("The given previous node must inLinkedList.")
            return

        #  2. create new node &
        #      Put in the data
        new_node = Node(new_data)

        # 4. Make next of new Node as next of prev_node
        new_node.next = prev_node.next

        # 5. make next of prev_node as new_node
        prev_node.next = new_node

    # Utility function to print the linked list

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next


# Code execution starts here
if __name__ == "__main__":

    # Start with the empty list
    llist = LinkedList()

    llist.push(6)
    llist.push(5)
    llist.push(4)
    llist.push(3)
    llist.push(2)

    print("Created linked list is: ")
    llist.printList()

    # Insert 1, after 2.
    llist.insertAfter(llist.head, 1)

    print("\nAfter inserting 1 after 2: ")
    llist.printList()