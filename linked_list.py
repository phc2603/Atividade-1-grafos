class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def insertElement(self, value):
        newNode = Node(value)
        if (self.head is None):
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.length += 1

    def getIndex(self):
        aux = self.tail
        if (aux.next is None):
            return 0

    def get(self, index):
        if (index == -1):
            return self.tail
        elif (index < 0 or index >= self.length):
            return None
        else:
            current = self.head
            for i in range(index):
                current = current.next
            return current
    
    def popFirst(self):
        if (self.length == 0):
            return None
        poppedNode = self.head
        if (self.length == 1):
            self.length -= 1
            self.removeHeadAndTail()
            return poppedNode
        else:
            self.head = self.head.next
            poppedNode.next = None
            self.length -= 1
            return poppedNode
    
    def pop(self):
        if (self.length == 0):
            return None
        poppedNode = self.tail
        if (self.length == 1):
            self.length -= 1
            self.removeHeadAndTail()
            return poppedNode
        else:
            tmp = self.head
            while tmp.next is not self.tail:
                tmp = tmp.next
            self.tail = tmp
            tmp.next = None
            self.length -= 1
            return poppedNode
        
    def removeHeadAndTail(self):
        self.head = None
        self.tail = None

    def removeElementbyIndex(self, index):
        if (index == 0):
            return self.popFirst()
        elif (index >= self.length or index < 0):
            return None
        elif (index == (self.length - 1) or (index == -1)):
            return self.pop()
        else:
            prevNode = self.get(index-1)
            poppedNode = prevNode.next #Nó que será removido
            prevNode.next = poppedNode.next
            poppedNode = None
            self.length -= 1
            return poppedNode
    
    def removeElementbyValue(self, value):
        current_node = self.head

        if (self.head.value == value):
            return self.popFirst()

        if (self.tail.value == value):
            return self.pop()    

        while current_node is not None:
            if current_node.value == value:
                prev_node.next = current_node.next
                current_node = None
                self.length -= 1
                break
            prev_node = current_node
            current_node = current_node.next

        print("Algo deu errado")
        return 


