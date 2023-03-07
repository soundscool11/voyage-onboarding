class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        if not self.head:
            self.head = ListNode(val, None)
            return
        
        node = self.head
        while node.next:
            node = node.next

        node.next = ListNode(val, None)

    def delete(self, val):
        temp = self.head
        if temp is not None:
            if temp.data == val:
                self.head = temp.next
                temp = None
                return
            
        while temp is not None:
            if temp.data == val:
                break
            prev = temp
            temp = temp.next

        if temp == None:
            return
        
        prev.next = temp.next
        temp = None

list = [1, 2, 3]
l1 = LinkedList()
for e in list:
    l1.append(e)
print(l1)