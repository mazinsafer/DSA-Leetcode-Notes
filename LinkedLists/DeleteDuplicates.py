## check if we have curr and cur.next because if we dont have cur.next (cur.next = None) theres no chance of duplicate
## if the current node is equal to curr.next, we want to skip it by setting curr = cur.next.next
## now that you have deleted duplicates for the curr node you can safely assign curr = curr.next
## then return the head


class Solution(object):
    def deleteDuplicates(self, head):
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head