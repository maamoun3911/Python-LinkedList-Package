from typing import Optional

class Node:
    def __init__(self, val=0) -> None:
        self.val = val
        self.next = None

class LList:
    def __init__(self) -> None:
        self.head = None
    
    # insert functions group
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
                    pre.next = self.__swapping2Dimensions(newNode, pre.next)
                    break
                pre = pre.next 
                counting += 1
            if counting == self.__linkedListlength():
                print("Sorry, but the key you entered isn't availabel")
    def insert_at_the_begging(self, val) -> None:
        newNode = Node(val)
        self.head = self.__swapping2Dimensions(newNode, self.head)
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
    
    # Delete functions group
    def delete_from_the_begging(self) -> None:
        if not self.head:
            print("Empty Linked List")
        self.head = self.head.next
    def delete_from_the_end(self) -> None:
        if not self.head:
            print("Empty Linked List")
        pre, curr = self.head, self.head.next
        while curr.next:
            curr, pre = curr.next, pre.next
        pre.next = curr.next
    def delete_from_the_middle(self, data) -> None:
        if not self.head:
            print("Empty Linked List")
        elif self.head.val == data:
            self.head = self.head.next
        pre, curr = self.head, self.head.next
        while curr:
            if curr.val == data:
                pre.next = curr.next
                break
            curr, pre = curr.next, pre.next
    def delete(self):
        self.head = None

    # Update functions group
    def update_first_element(self, data) -> None:
        if not self.head: print("Empty Linked List")
        elif self.head:
            self.head.val = data
    
    def update_last_element(self, data) -> None:
        if not self.head: print("Empty Linked List")
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.val = data
    
    def update_a_middle_element(self, element, data) -> None:
        if not self.head: print("Empty Linked List")
        elif self.head.val == element:
            self.head.val = data
            return
        curr = self.head
        while curr:
            if curr.val == element:
                curr.val = data
                return
            curr = curr.next

    # Length
    def length(self) -> int:
        print(self.__linkedListlength())
    
    # Overviw
    def overview(self) -> str:
        if not self.head:
            print("Empty Linked List")
        curr = self.head
        while curr:
            print(curr.val, end=" ")
            curr = curr.next
            if curr:
                print(" -> ", end=" ")
            else:
                print()
                return
    
    # View element
    def view_element(self, data) -> str:
        if not self.head:
            print("Empty Linked List")
        counter: int = 0
        curr = self.head
        while curr:
            if curr.val == data:
                print(f"type: {type(curr.val)}, next element: {curr.next}, element order: {counter}")
                print(f"The element: {curr.val}")
                break
            curr = curr.next
            counter += 1

    # helper methods
    
    # swapping functions
    def __swapping2Dimensions(self, newNode: Node, nextNode: Node) -> Optional[Node]:
        newNode.next = nextNode
        return newNode
    
    def __linkedListlength(self) -> int:
        lengthCounter: int = 0
        curr = self.head
        while curr:
            lengthCounter += 1
            curr = curr.next
        return lengthCounter
