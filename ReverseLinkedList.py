## 3 pointers: current node, prev node, and next node
## initially prev is pointing to nothing, and curr is at the head
## want the head to point to nothing, so curr.next (head) = prev (nothing)
## next_node is a temporary value equal to the next node which is curr.next
## happening in a while loop where curr is a node
## eventually curr and next_node will be nothing, and prev will be the head of the new 
## return prev b/c its the head now

class Solution(object):
    def reverseList(self, head):
        curr = head
        prev = None
        next_node = None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev