class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        return str(self.val)

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        cur = self.head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def __contains__(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.val == item:
                found = True
            else:
                current = current.next
        return found

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        temp = Node(item)
        temp.next = self.head
        self.head = temp

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.val == item:
                found = True
            else:
                previous = current
                current = current.next
        if previous == None:
            self.head = current.next
        else:
            previous.next=current.next

