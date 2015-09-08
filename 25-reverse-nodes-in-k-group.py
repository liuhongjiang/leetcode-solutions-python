# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def pushToStack(self, current, k):
        stack = []
        while k > 0 and current is not None:
            stack.append(current)
            current = current.next
            k -= 1
        return stack

    def reverseStack(self, stack, previous):
        if previous is None:
            previous = stack.pop()
        else:
            previous.next = stack.pop()
            previous = previous.next
        for node in stack:
            node.next = previous.next
            previous.next = node

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k <= 1:
            return head

        stack = self.pushToStack(head, k)
        if len(stack) < k:
            return head

        next_previous = stack[0]
        ret_head = stack[k - 1]
        previous = None
        self.reverseStack(stack, previous)

        while next_previous is not None:
            previous = next_previous
            stack = self.pushToStack(previous.next, k)
            if len(stack) < k:
                return ret_head

            next_previous = stack[0]
            self.reverseStack(stack, previous)

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
    print_link(solution.reverseKGroup(list2link([2, 7, 8, 9, 5, 4, 1, 2]), 3))
    print_link(solution.reverseKGroup(list2link([1, 2, 3, 4, 5]), 2))
    print_link(solution.reverseKGroup(list2link([1, 2, 3, 4, 5]), 3))
