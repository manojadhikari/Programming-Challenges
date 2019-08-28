#Given a linked list, determine if it has a cycle it in. 

#Time: O(n). Space: O(1)
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        slow = dummy
        fast = dummy
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next

            if slow == fast:
                return True

        return False
    
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)

a.next = b
b.next = c
c.next = d
d.next = None

solution_obj = Solution()
result = solution_obj.detectCycle(a)
print (result)





