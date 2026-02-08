# class MyLinkedList:
#     class Node:
#         def __init__(self, data):
#             self.data=data
#             self.next=None

#     def __init__(self):
#         self.head=self.Node(0)
#         self.size=0
        
        

#     def get(self, index: int) -> int:
#         if self.size == 0 or index>=self.size or index<0:
#             return -1
#         else:
#             cur=self.head
#             for i in range(index):
#                 cur=cur.next
#             return cur.data
        

#     def addAtHead(self, val: int) -> None:
#         Question=self.Node(val)
#         Question.next=self.head
#         head=Question
#         self.size+=1
        

#     def addAtTail(self, val: int) -> None: 
#         if self.size == 0:
#             addAtHead(val)
#         else:
#             cur=self.head
#             while cur.next!=None:
#                 cur=cur.next
            
#             cur.next=self.Node(val)
#             self.size+=1
        

#     def addAtIndex(self, index: int, val: int) -> None:
#         if index == 0:
#             addAtHead(val)
#         elif index == self.size:
#             addAtTail(val)
#         else:
#             cur=self.head
#             for i in range(0,index):
#                 cur=cur.next
#             New_Node=self.Node(val)
#             New_Node.next=cur.next
#             cur.next=New_Node
#             self.size+=1
            



        

#     def deleteAtIndex(self, index: int) -> None:
#         if self.size == 0 or index>=self.size or index<0:
#             return 
#         if index==0:
#             self.head=self.head.next
#             self.size-=1
#         else:
#             cur = self.head
#             for i in range(index):
#                 cur = cur.next
#             cur.next = cur.next.next
#             self.size-=1

        


# # Your MyLinkedList object will be instantiated and called as such:
# # obj = MyLinkedList()
# # param_1 = obj.get(index)
# # obj.addAtHead(val)
# # obj.addAtTail(val)
# # obj.addAtIndex(index,val)
# # obj.deleteAtIndex(index)

class MyLinkedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = self.Node(0)  # dummy head
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        
        cur = self.head.next
        for _ in range(index):
            cur = cur.next
        return cur.data

    def addAtHead(self, val: int) -> None:
        node = self.Node(val)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = self.Node(val)
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        
        cur = self.head
        for _ in range(index):
            cur = cur.next
        
        node = self.Node(val)
        node.next = cur.next
        cur.next = node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        
        cur = self.head
        for _ in range(index):
            cur = cur.next
        
        cur.next = cur.next.next
        self.size -= 1
