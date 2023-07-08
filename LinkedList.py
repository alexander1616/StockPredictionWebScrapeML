from pdb import set_trace as bp

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        if self.next is None:
            return str(self.data)
        else:
            return str(self.data) + " -> " + str(self.next)

class LinkedList:
    def __init__(self):
        self.head = None
        #self._findprev = None #temp var created by find
        self._count = 0

    def __repr__(self):
        if self.head is None:
            return "No data"
        else:
            return str(self.head)
    
    def __getitem__(self, index):
        if self._count == 0:
            raise Exception("No data in list")
        if index < 0:
            print("Negative index not supported")
            return
        if index > self._count:
            raise Exception("Index out of range")

        temp = self.head
        track = 0
        while temp is not None:
            if track == index:
                return temp.data
            temp = temp.next
            track +=1

    def __setitem__(self, index, data):
        if self._count == 0:
            raise Exception("No data in list")
        if index < 0:
            print("Negative index not supported")
            return
        if index > self._count:
            raise Exception("Index out of range")
        
        temp = self.head
        track = 0
        while temp is not None:
            if track == index:
                temp.data = data
                return
            temp = temp.next
            track +=1

    def count(self):
        return self._count

    def __len__(self):
        return self._count

    def insert(self, data, index = 0):
        newNode = Node(data)

        if self._count == 0:
            newNode.next = self.head
            self.head = newNode
            self._count += 1
            return

        if index >= self._count:
            index = self._count -1
        elif index < 0:
            index += self._count
            if index < 0:
                index = 0
        #bp()
        temp = self._iterHelper(index)
        if self._findprev is None:
            newNode.next = self.head
            self.head = newNode
        else:
            if temp.next is None:
                temp.next = newNode
            else: 
                newNode.next = temp
                self._findprev.next = newNode
        self._count += 1    
        return

    def insert2(self, data, index = 0):
        if index < 0 or index > self._count:
            print("Invalid Index")
            return

        newNode = Node(data)

        if index == 0:
            newNode.next = self.head
            self.head = newNode
        else:
            temp = self.head
            track = 0
            while track < index - 1:
                temp = temp.next
                track += 1
            newNode.next = temp.next
            temp.next = newNode

        self._count += 1    

    def append(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            temp = self.head
            while temp.next is not None:
                self._findprev = temp
                temp = temp.next
            temp.next = newNode
        self._count += 1
            
    def print(self):
        if self.head is None:
            print("There is no data.")
        else:
            temp = self.head
            while temp is not None:
                print(temp.data)
                temp = temp.next
    
    def _findHelper(self, data):
        self._findprev = None
        temp = self.head
        while temp is not None:
            if temp.data == data:
                return temp
            else:
                self._findprev = temp
                temp = temp.next
        return None

    def _iterHelper(self, index):
        if (index >= self._count) or (index < -self._count):
            raise Exception("Index Error")
        if index < 0:
            index = index + self._count
        self._findprev = None
        temp = self.head
        track = 0
        while track < index:
            self._findprev = temp
            temp = temp.next
            track += 1
        return temp

    def find(self, data):
        return self._findHelper(data)

    def delete(self, data):
        temp = self._findHelper(data)
        if temp is not None:
            if self._findprev is None:
                self.head = temp.next
            else:
                self._findprev.next = temp.next
            self._count -= 1
    
    def reverse2(self):
        temp = self.head
        self.head = None
        self._count = 0
        while temp is not None:
            self.insert(temp.data)
            temp = temp.next

    def reverse(self):
        temp = self.head
        prev = None
        while temp is not None:
            x = temp.next
            temp.next = prev
            prev = temp
            temp = x
        self.head = prev

# Test Cases

def test1():
    dadList = LinkedList()
    dadList.insert('first insert')
    dadList.insert('second insert')
    dadList.append('first append')
    dadList.append('second append')
    return dadList

