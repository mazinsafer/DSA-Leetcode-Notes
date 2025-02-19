## set a dummy node where its parameters are set in the class
## dummy node is going to be be the current node/head, its value will be manipulated in the problem
## in a while loop where L1 and L2 are lists with nodes, check if the val of L1/L2 is less than L1/L2
## which ever one is smaller you want to first set curr.next = to and then set curr = to
## then set L1/L2 = L1/L2.next for the next iteration, and repeat
## at the end of the loop, we will be missing L1, L2, or both so set curr.next = L1 if L1 exists, if not then L2
## return d.next
class ListNode(object):
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        d = ListNode()
        cur = d
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                cur = list1
                list1 = list1.next
            else:
                cur.next = list2
                cur = list2
                list2 = list2.next

        cur.next = list1 if list1 else list2
        return d.next

# Time Complexity: O(n)
# Space Complexity: O(1)