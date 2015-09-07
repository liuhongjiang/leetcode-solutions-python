# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2

        ret_head = l1
        carry = 0

        while l1 is not None and l2 is not None:
            tmp = l1.val + l2.val + carry
            carry = tmp / 10
            l1.val = tmp % 10
            if l1.next is None or l2.next is None:
                break
            l1 = l1.next
            l2 = l2.next

        if l1.next is None:
            l1.next = l2.next

        while carry != 0:
            if l1.next is None:
                l1.next = ListNode(0)
            l1 = l1.next
            tmp = l1.val + carry
            l1.val = tmp % 10
            carry = tmp / 10

        return ret_head


def list2link(l):
    if len(l) == 0:
        return None
    ret_tail = ret_head = ListNode(l[0])
    for val in l[1:]:
        tmp = ListNode(val)
        ret_tail.next = tmp
        ret_tail = ret_tail.next
    return ret_head


def print_link(link):
    while link is not None:
        print "->%d" % link.val,
        link = link.next
    print "\n"


if __name__ == '__main__':
    solution = Solution()
    print_link(solution.addTwoNumbers(list2link([2, 7, 8, 9, 9, 9]), list2link([3, 7, 5])))
    print_link(solution.addTwoNumbers(list2link([2, 4, 3]), list2link([5, 6, 4])))
