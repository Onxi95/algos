class Node:
    def __init__(self, value: int = 0, next: Optional[Node] = None):
        self.value = value
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.beginning = Node()
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        current = self.beginning
        for _ in range(index):
            current = current.next

        return current.next.value

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        next_node = self.beginning.next
        self.beginning.next = new_node
        new_node.next = next_node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        current = self.beginning
        while current.next:
            current = current.next
        current.next = Node(val)
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return -1
        current = self.beginning
        for _ in range(index):
            current = current.next
        next_node = current.next
        new_node = Node(val)
        current.next = new_node
        new_node.next = next_node
        self.size += 1
        

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return -1
        current = self.beginning
        for _ in range(index):
            current = current.next

        current.next = current.next.next
        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)