# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def listLength(self):
        currNode = self.head
        length = 0
        while currNode is not None:
            length += 1
            currNode = currNode.next
        return length
        
    def insertHead(self, newNode):
        tempNode = self.head
        self.head = newNode
        self.head.next = tempNode
        del tempNode
        
    def insertEnd(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            currNode = self.head
            while True:
                if currNode.next is None:
                    break
                currNode = currNode.next
            currNode.next = newNode
            
    def insertAt(self, newNode, position):
        if position < 0 and position > self.listLength():
            print("Invalid position")
            return
        if position == 0:
            self.insertHead(newNode)
            return
        currNode = self.head
        currPosition = 0
        while True:
            if currPosition == position:
                prevNode.next = newNode
                newNode.next = currNode
                break
            prevNode = currNode 
            currNode = currNode.next
            currPosition += 1
        
    def deleteEnd(self):
        currNode = self.head
        while currNode.next is not None:
            prevNode = currNode
            currNode = currNode.next
        prevNode.next = None
            
    
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

# ll = LinkedList()
# firstNode = Node(10)
# ll.insertEnd(firstNode)
# secondNode = Node(20)
# ll.insertEnd(secondNode)
# thirdNode = Node(15)
# ll.insertAt(thirdNode, 1)
# fourthNode = Node(17)
# ll.insertAt(fourthNode, 2)
# ll.printList()

ll = LinkedList()
firstNode = Node("John")
ll.insertEnd(firstNode)
secondNode = Node("Liam")
ll.insertEnd(secondNode)
thirdNode = Node("Matt")
ll.insertHead(thirdNode)
ll.printList()
print()

ll.deleteEnd()
ll.printList()