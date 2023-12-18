# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def createList(self, items:list) -> ListNode:
        last = None
        print(items)
        for i in range(len(items)):
            if i==0:
                node = ListNode(items[i],None)
                last = node
            else:
                node = ListNode(items[i], last)
                last = node
            print(last)
        return last
            
    def reverse(self, head:ListNode) -> ListNode:
        prev, curr = None, head
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
    
    def getVal(self, head:ListNode) -> int:
        curr = head
        s = ''
        while curr:
            s += str(curr.val)
            curr = curr.next
        return int(s)
            
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        l1_int = self.getVal(self.reverse(l1))
        l2_int = self.getVal(self.reverse(l2))
        
        s = str(l1_int+l2_int)
        out = self.createList(s)
        return out
        
# Runtime 230 ms Beats 6% Memory 14.5 MB Beats 100%
