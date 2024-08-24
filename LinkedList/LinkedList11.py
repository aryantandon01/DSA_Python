from LinkedList10 import Node, LinkedList

def mergeLists(firstList, secondList, mergedList):
    currentFirst = firstList.head
    currentSecond = secondList.head
    while True:
        if currentFirst is None:
            mergedList.insertEnd(currentSecond)
            break
        if currentSecond is None:
            mergedList.insertEnd(currentFirst)
        if currentFirst.data < currentSecond.data:
            nextFirst = currentFirst.next
            currentFirst.next = None
            mergedList.insertEnd(currentFirst)
            currentFirst = nextFirst
        else:
            nextSecond = currentSecond.next
            currentSecond.next = None
            mergedList.insertEnd(currentSecond)
            currentSecond = nextSecond
    return mergedList

nodeOne = Node(1)
nodeTwo = Node(3)
nodeThree = Node(4)
ll1 = LinkedList()
ll1.insertEnd(nodeOne)
ll1.insertEnd(nodeTwo)
ll1.insertEnd(nodeThree)

nodeFour = Node(2)
nodeFive = Node(7)
nodeSix = Node(9)
ll2 = LinkedList()
ll2.insertEnd(nodeFour)
ll2.insertEnd(nodeFive)
ll2.insertEnd(nodeSix)
print("Printing First List")
ll1.printList()
print("Printing Second List")
ll2.printList()

mergedList = LinkedList()
mergedList = mergeLists(ll1, ll2, mergedList)
print("Printing Merged List")
mergedList.printList()