## O(n) time O(1) space
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def middleNode(self, head):
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    

## slow pointer fast pointer approach
## set slow and fast = to the head
## for every step slow takes, fast takes two steps
## in while loop where fast.next and fast.next.next because we want to break out of the loop when fast cant proceed
## slow will end up being the middle
## return slow