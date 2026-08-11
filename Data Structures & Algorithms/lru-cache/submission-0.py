class LRUCache:

    class Node:
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.next = None
            self.prev = None

    def __init__(self, capacity: int):
        self.cap = capacity
        self.mp = {}
        self.head = self.Node(-1, -1)
        self.tail = self.Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head


    def addNode(self, key, node):
        nxt = self.head.next
        node.next = nxt
        node.prev = self.head
        self.head.next = node
        nxt.prev = node
        self.mp[key] = node

    def delNode(self, node):
        nxt = node.next
        prev = node.prev
        prev.next = nxt
        nxt.prev = prev

    def get(self, key: int) -> int:
        if key not in self.mp:
            return -1
        node = self.mp[key]

        self.delNode(node)
        self.addNode(node.key, node)

        return node.val

    def put(self, key: int, value: int) -> None:
        
        if key in self.mp:
            node = self.mp[key]

            self.delNode(node)
            del self.mp[node.key]
        if self.cap == len(self.mp):
            lru = self.tail.prev

            self.delNode(lru)
            del self.mp[lru.key]

        node = self.Node(key, value)
        self.addNode(key, node)
