# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            total = carry

            if l1 is not None:
                total += l1.val
                l1 = l1.next

            if l2 is not None:
                total += l2.val
                l2 = l2.next

            if total >= 10:
                carry = 1
            else:
                carry = 0

            digit = total % 10

            current.next = ListNode(digit)
            current = current.next

        return dummy.next


# Create Linked List
def createList(values):
    dummy = ListNode(0)
    current = dummy

    for value in values:
        current.next = ListNode(value)
        current = current.next

    return dummy.next


# Print Linked List
def printList(head):
    while head is not None:
        print(head.val, end="")

        if head.next is not None:
            print(" -> ", end="")

        head = head.next

    print()


# Main Function
if __name__ == "__main__":

    # First Number: 342
    l1 = createList([2, 4, 3])

    # Second Number: 465
    l2 = createList([5, 6, 4])

    solution = Solution()

    result = solution.addTwoNumbers(l1, l2)

    print("First Number:")
    printList(l1)

    print("Second Number:")
    printList(l2)

    print("Result:")
    printList(result)
