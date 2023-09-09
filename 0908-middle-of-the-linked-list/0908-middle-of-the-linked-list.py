# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head 
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next 
        if fast.next: slow = slow.next
        return slow 
        # 1 node 1 slow fast 
        # 2 node 1 slow fast, 2
        # 3 node 1, 2 slow,3 fast
        # 4 node 1, 2 slow, 3 fast, 4
        # 5 node 1, 2, 3 slow, 4, 5 fast 
        # 6 node 1, 2, 3 slow, 4, 5 fast, 6
            