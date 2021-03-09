# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


class Solution:
    def removeKthNodeFromEnd(self, head, k):
        # Time O(n) || Space O(n)
        first = head
        second = head
        counter = 1
        while counter <= k:
            second = second.next
            counter += 1

        if second is None:
            head.value = head.next.value
            head.next = head.next.next
            return

        while second.next is not None:
            second = second.next
            first = first.next

        first.next = first.next.next
        return
