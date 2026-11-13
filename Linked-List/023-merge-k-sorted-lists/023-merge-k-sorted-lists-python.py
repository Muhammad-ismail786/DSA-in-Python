
import heapq
from itertools import count


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """

        min_heap = []
        counter = count()

        # Add the first node of every non-empty list
        for node in lists:
            if node is not None:
                heapq.heappush(
                    min_heap,
                    (node.val, next(counter), node)
                )

        # Create dummy node
        dummy = ListNode(0)
        current = dummy

        # Merge all linked lists
        while min_heap:

            # Get the smallest node
            value, _, smallest = heapq.heappop(min_heap)

            # Attach node to result
            current.next = smallest
            current = current.next

            # Add next node from the same list
            if smallest.next is not None:
                heapq.heappush(
                    min_heap,
                    (smallest.next.val, next(counter), smallest.next)
                )

        return dummy.next


# Helper function to create linked list
def createLinkedList(values):

    dummy = ListNode(0)
    current = dummy

    for value in values:
        current.next = ListNode(value)
        current = current.next

    return dummy.next


# Helper function to print linked list
def printLinkedList(head):

    while head is not None:
        print(head.val, end="")

        if head.next is not None:
            print(" -> ", end="")

        head = head.next

    print()


# Main function
if __name__ == "__main__":

    # First list: 1 -> 4 -> 5
    list1 = createLinkedList([1, 4, 5])

    # Second list: 1 -> 3 -> 4
    list2 = createLinkedList([1, 3, 4])

    # Third list: 2 -> 6
    list3 = createLinkedList([2, 6])

    lists = [list1, list2, list3]

    solution = Solution()

    result = solution.mergeKLists(lists)

    print("Merged Linked List:")
    printLinkedList(result)
