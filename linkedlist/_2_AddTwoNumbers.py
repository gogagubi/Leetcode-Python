from model.listnode import ListNode


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode()
        node = result

        reminder, calc = 0, 0
        while l1 != None or l2 != None or reminder > 0:
            calc = 0

            if l1 != None:
                calc += l1.val
                l1 = l1.next

            if l2 != None:
                calc += l2.val
                l2 = l2.next

            calc += reminder
            node.next = ListNode(calc % 10)
            reminder = calc // 10

            node = node.next

        return result.next


if True:
    l1 = ListNode()
    l1.setArgs(2, 4, 3)

    l2 = ListNode()
    l2.setArgs(5, 6, 4)

    s = Solution()
    res = s.addTwoNumbers(l1, l2)
    res.show()

if True:
    l1 = ListNode()
    l1.setArgs(0, 8, 6, 5, 6, 8, 3, 5, 7)

    l2 = ListNode()
    l2.setArgs(6, 7, 8, 0, 8, 5, 8, 9, 7)

    s = Solution()
    res = s.addTwoNumbers(l1, l2)
    res.show()

if True:
    l1 = ListNode()
    l1.setArgs(9)

    l2 = ListNode()
    l2.setArgs(1, 9, 9, 9, 9, 9, 9, 9, 9)

    s = Solution()
    res = s.addTwoNumbers(l1, l2)
    res.show()
