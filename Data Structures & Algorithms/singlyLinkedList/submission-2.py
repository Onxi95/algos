class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        ptr = self.head
        for _ in range(index):
            ptr = ptr.next_node

        return ptr.data

    def insertHead(self, val: int) -> None:
        node = Node(val, self.head)
        self.head = node
        if self.size == 0:
            self.tail = node
        self.size += 1

    def insertTail(self, val: int) -> None:
        node = Node(val)
        if self.size == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next_node = node
            self.tail = node
        self.size += 1

    def remove(self, index: int) -> bool:
        if index < 0 or index >= self.size:
            return False

        if index == 0:
            self.head = self.head.next_node
            if self.size == 1:
                self.tail = None
            self.size -= 1
            return True

        ptr = self.head
        for _ in range(index - 1):
            ptr = ptr.next_node

        target = ptr.next_node
        ptr.next_node = target.next_node
        if target == self.tail:
            self.tail = ptr
        self.size -= 1
        return True

    def getValues(self) -> list[int]:
        vals = []
        ptr = self.head
        while ptr:
            vals.append(ptr.data)
            ptr = ptr.next_node
        return vals
