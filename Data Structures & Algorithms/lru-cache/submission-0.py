class Node():
    def __init__(self, key=0, val=0, prev = None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.d = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity


    def get(self, key: int) -> int:

        if key not in self.d: return -1

        node = self.d[key]
        self._make_latest(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:

        if key in self.d:
            node = self.d[key]
            node.val = value
            self._make_latest(node)
            return

        if len(self.d) >= self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            self.d.pop(lru.key)

        new = Node(key, value, next=self.head)
        self._add_front(new)
        self.d[key] = new
                

    def _add_front(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _make_latest(self, node):
        self._remove(node)
        self._add_front(node)