## O(n) time O(1) space

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        slow = head
        fast = head
        for i in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return head
    
    ## slow-fast algorithim:
    ## set slow and fast and head of the list as well as a counter i
    ## keep moving fast forward  until fast is at the node we want to remove
    ## if we end up needing to remove the head, return head.next
    ## now keep moving slow and fast forward until fast reaches the end and slow ends up being at the node before the node we want to remove
    ## when the loop breaks, set slow.next = to slow.next.next to skip the node and return the head