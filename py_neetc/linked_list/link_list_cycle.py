
class ListNode:
     def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head) -> bool:

        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast==slow:
                return True

        return False


if __name__=='__main__':
    print ("Start")

    head = ListNode(10)
    n1 = ListNode(5)
    n2 = ListNode(21)
    n3 = ListNode(7)
    n4 = ListNode(4)
    n5 = ListNode(3)

    head.next=n1
    n1.next=n2
    n2.next=n3
    n3.next=n1
    n4.next=n5

    s = Solution()
    f = s.hasCycle(head)
    print ("\nfound cycle? ",f)
    
    print ("END")