from model.listnode import ListNode


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        result: ListNode = None

        while head != None:
            newHead = head.next
            head.next = result
            result = head
            head = newHead

        return result


if True:
    listNode = ListNode()
    listNode.setArgs(1, 2, 3, 4, 5)

    s = Solution()
    res = s.reverseList(listNode)
    res.show()

if True:
    listNode = ListNode()
    listNode.setArgs(43, 12, 5, 2, 24)

    s = Solution()
    res = s.reverseList(listNode)
    res.show()
