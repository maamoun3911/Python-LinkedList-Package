from typing import Optional

class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

class LList:
    def __init__(self) -> None:
        self.head = None
    
    # insert function group
    def append(self, val) -> None:
        if not self.head:
            self.head = Node(val)
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = Node(val)
    def insert_at_the_end(self, val) -> None:
        self.append(val)
    def insert_between_nodes(self, previous, val) -> str:
        counting: int = 0
        if not self.head:
            print("Empty Linked List")
        else:
            newNode = Node(val)
            pre = self.head
            while pre:
                if pre.val == previous:
                    newNode.next = pre.next
                    pre.next = newNode
                    break
                pre = pre.next 
                counting += 1
            if counting == self.length():
                print("Sorry, but the key you entered isn't availabel")
    def insert_at_the_begging(self, val) -> None:
        newNode = Node(val)
        newNode.next = self.head
        self.head = newNode
    def sorted_insertion(self, val) -> str:
        newNode = Node(val)
        if not self.head: self.head = self.__swapping2Dimensions(newNode, self.head)
        elif not self.head.next:
            if self.head.val > val: self.head = self.__swapping2Dimensions(newNode, self.head)
            else: self.head.next = newNode
        elif self.head.next and self.head.val > val:
            self.head = self.__swapping2Dimensions(newNode, self.head)
            return
        pre, curr = self.head, self.head.next
        while curr:
            if curr.val > val:
                pre.next = self.__swapping2Dimensions(newNode, curr)
                return
            pre, curr = pre.next, curr.next

    # helper methods
    
    # swapping functions
    def __swapping2Dimensions(self, newNode: Node, nextNode: Node) -> Optional[Node]:
        newNode.next = nextNode
        return newNode

    # Length
    def length(self) -> int:
        lengthCounter: int = 0 
        curr = self.head
        while curr:
            lengthCounter += 1
            curr = curr.next
        return lengthCounter
    
    # Overviw
    def overview(self):
        if not self.head:
            print("Empty Linked List")
        curr = self.head
        while curr:
            print(curr.val, end=" ")
            curr = curr.next
            if curr:
                print(" -> ", end=" ")

LinkedList = LList()
LinkedList.append(0)
LinkedList.insert_between_nodes(0, 1)
LinkedList.append(3)
LinkedList.insert_at_the_begging(-1)
LinkedList.insert_at_the_end(9)
LinkedList.sorted_insertion(-2)
LinkedList.overview()
