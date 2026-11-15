
from __future__ import annotations

from typing import Optional


# Definition for singly linked list
class ListNode:
    def __init__(
        self,
        val: int = 0,
        next: Optional[ListNode] = None
    ) -> None:
        self.val: int = val
        self.next: Optional[ListNode] = next


class Solution:

    def reverseKGroup(
        self,
        head: Optional[ListNode],
        k: int
    ) -> Optional[ListNode]:

        # Step 1: Check if k nodes are available
        temp: Optional[ListNode] = head

        for i in range(k):
            if temp is None:
                return head

            temp = temp.next

        # Step 2: Reverse k nodes
        prev: Optional[ListNode] = None
        curr: Optional[ListNode] = head

        for i in range(k):

            # Save next node
            assert curr is not None
            next_node: Optional[ListNode] = curr.next

            # Reverse current node's link
            curr.next = prev

            # Move pointers forward
            prev = curr
            curr = next_node

        # Step 3: Connect remaining nodes
        assert head is not None
        head.next = self.reverseKGroup(curr, k)

        # Step 4: Return new head
        return prev


# Print linked list
def printList(head: Optional[ListNode]) -> None:

    while head is not None:
        print(head.val, end="")

        if head.next is not None:
            print(" -> ", end="")

        head = head.next

    print()


# Main function
if __name__ == "__main__":

    n = int(input("Enter number of nodes: "))

    head: Optional[ListNode] = None
    tail: Optional[ListNode] = None

    print("Enter node values:")

    for i in range(n):

        value = int(input())

        new_node = ListNode(value)

        if head is None:
            head = new_node
            tail = new_node

        else:
            assert tail is not None
            tail.next = new_node
            tail = new_node

    k = int(input("Enter k: "))

    print("\nOriginal List: ", end="")
    printList(head)

    solution = Solution()

    head = solution.reverseKGroup(head, k)

    print("After Reversing: ", end="")
    printList(head)
