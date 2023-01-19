'''
https://leetcode.com/problems/linked-list-cycle-ii
142. Linked List Cycle II

Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by 
continuously following the next pointer. Internally, pos is used to denote the index of the node 
that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that 
pos is not passed as a parameter.

Do not modify the linked list.

'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head) -> bool:

        if head==None or head.next==None:
            return None

        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast==slow:
                break #found a cycle

        if slow==fast:
            #found that theres a cycle somewhere 
            tmp = head
            while tmp!=slow:
                tmp = tmp.next
                slow = slow.next

            return slow
        else:
            return None


if __name__=='__main__':
    print ("Start")

    n3 = ListNode(3)
    n2 = ListNode(2)
    n0 = ListNode(0)
    nm4 = ListNode(-4)

    n3.next=n2
    n2.next=n0
    n0.next=nm4
    nm4.next=n2
 
    s = Solution()
    f = s.detectCycle(n3)
    print ("\nDetect Cycle:= ",f)
 
    print ("END")