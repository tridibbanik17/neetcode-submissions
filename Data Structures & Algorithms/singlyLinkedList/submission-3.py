class ListNode:
    def __init__(self, val:int):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.size = 0
    
    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.val

    def insertHead(self, val: int) -> None:
        node = ListNode(val)
        node.next = self.head
        self.head = node
        self.size += 1
        return 

    def insertTail(self, val: int) -> None:
        node = ListNode(val)
        if self.head is None:
            self.head = node
        else:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            curr.next = node
        self.size += 1

    def remove(self, index: int) -> bool:
        if index < 0 or index >= self.size:
            return False
        curr = self.head
        if index == 0:
            self.head = curr.next 
        else: 
            for _ in range(index-1):
                curr = curr.next
            curr.next = curr.next.next
        self.size -= 1
        return True

    def getValues(self) -> List[int]:
        new_list = []
        curr = self.head
        for _ in range(self.size):
            new_list.append(curr.val)
            curr = curr.next
        return new_list
        
