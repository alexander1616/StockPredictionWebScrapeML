#Double Linked List
from pdb import set_trace as bp

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.back = None

    def __repr__(self):
        return str(self.data)

class DLink: 
    def __init__(self):
        self.head = None
        self.tail = None
        self._count = 0

    def __repr__(self):
        if self.head is None:
            return "No data"
        
        forward_str = "Forward Traverse: "
        reverse_str = "Reverse Traverse: "

        temp = self.head
        while temp is not None:
            forward_str += str(temp.data) + " -> "
            temp = temp.next
        forward_str += "None"

        temp2 = self.tail
        while temp2 is not None:
            reverse_str += str(temp2.data) + " -> "
            temp2 = temp2.back
        reverse_str += "None"

        return forward_str + "\n" + reverse_str

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
            self.head = newNode
            self.tail = newNode
            self._count = 1
            return

        if index >= self._count:
            index = self._count -1
        elif index < 0:
            index += self._count
            if index < 0:
                index = 0
        #bp()
        temp = self._iterHelper(index)
        if temp.back is None:
            newNode.next = self.head
            self.head.back = newNode
            self.head = newNode
        else:
            if temp.next is None:
                temp.next = newNode
                newNode.back = temp
                self.tail = newNode
            else: 
                newNode.next = temp
                temp.back.next = newNode
                newNode.back = temp.back
                temp.back = newNode
        self._count += 1    
        return

    def append(self, data):
        self.insert(data, self._count)

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
            if temp.back is None:
            # beginning
                self.head = temp.next
                temp.next.prev = None
                if self.tail == temp:
                    self.tail = None
            elif temp.next is None:
            # last
                self.tail = temp.back
                temp.back.next = None
            else:
                temp.back.next = temp.next
                temp.next.back = temp.back
            self._count -= 1
    
# Test Cases

def unittest1():
    dList = DLink()
    dList.insert('first insert')
    dList.insert('second insert')
    dList.append('first append')
    dList.append('second append')
    return dList

