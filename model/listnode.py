class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def setArgs(self, *args):
        self.val = args[0]
        tmp = self

        for i in args[1:]:
            newNode = ListNode(i)
            tmp.next = newNode
            tmp = tmp.next

    def show(self):
        tmp = self
        while tmp != None:
            print(tmp.val, sep=' ', end=' ', flush=True)
            tmp = tmp.next

        print()
