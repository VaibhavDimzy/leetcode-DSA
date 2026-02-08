# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) :

        #APPROACH 2 slow and fast pointers

        slow=head
        fast=head

        while fast!= None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next

        return slow
    




    #     APPRAOCH 1
    #     count=self.getCount(head)

    #     curr=head
    #     for i in range(1,(count//2) + 1):
    #         curr=curr.next

        
    #     return curr



    
    # def getCount(self, head):
    #     # code here
    #     curr=head
    #     count=0
    #     while curr!=None:
    #         count+=1
    #         curr=curr.next
    #     return count
        