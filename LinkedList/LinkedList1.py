# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            currNode = self.head
            while True:
                if currNode.next is None:
                    break
                currNode = currNode.next
            currNode.next = newNode
    def printList(self):
        if self.head is None:
            print("List is Empty.")
            return
        currNode = self.head
        while True:
            if currNode is None:
                break
            print(currNode.data)
            currNode = currNode.next

ll = LinkedList()
firstNode = Node("John")
ll.insert(firstNode)
secondNode = Node("Liam")
ll.insert(secondNode)
ll.printList()