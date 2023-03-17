import collections

class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self):
        self.size = 1000
        self.table = collections.defaultdict(ListNode)

    def put(self, key, value):
        index = key % self.size

        new_node = ListNode(key, value)

        item = self.table[index]
        if not item:
            self.table[index] = new_node
            return

        while item:
            if item.key == key:
                item.value = value
                return 
            if not item.next:
                break
            item = item.next
        item.next = new_node

    def get(self, key):
        item = self.table[key]
        if not item:
            return -1
