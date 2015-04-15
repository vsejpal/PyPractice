__author__ = 'vsejpal@gmail.com'


class NthLast:
    '''  Finds the Nth Last Element of a linked list by calling findNthLast   '''

    def setupList(self):
        a = Node("A")
        b = Node("B")
        c = Node("C")
        d = Node("D")
        e = Node("E")

        a.next = b
        b.next = c
        c.next = d
        d.next = e

        return a

    def printList(self, head):
        while head != None:
            print head.data,
            if head.next != None:
                print " --> ",
            head = head.next

    def findNthLast(self, head, n):
        fast = head
        slow = head

        for i in range(0, n-1):
            print 'i = ' + str(i)
            fast = fast.next

        while fast.next != None:
            slow = slow.next
            fast = fast.next

        return slow.data



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


nth_last = NthLast()
head = nth_last.setupList()
nth_last.printList(head)
print ''
print nth_last.findNthLast(head, 2)





