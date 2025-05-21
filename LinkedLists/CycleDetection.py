## O(n) time O(1) space
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        d = ListNode()
        d = head
        slow = fast = d
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False


## Floyds Slow Pointer/Fast pointer algorithim
## initalize a dummy node, along with two pointers slow and fast = to the head
## when slow moves once, fast moves twice
## so this needs to happen in a while loop where fast is a node and fast.next is a node so you can move fast.next to fast.next.next
## if the while loop breaks and fast.next = None, it reaches the end of the list so return False because there is no cycle
## if there is a cycle, fast and slow will end up being the same the node, so when that happens return true