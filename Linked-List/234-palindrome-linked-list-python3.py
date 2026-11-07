
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        # Find the middle of linked list
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half
        prev = None
        curr = slow

        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # Compare both halves
        first = head
        second = prev

        while second is not None:
            if first.val != second.val:
                return False

            first = first.next
            second = second.next

        return True


# Main function
if __name__ == "__main__":

    # Hardcoded input: 1 -> 2 -> 2 -> 1
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(1)

    solution = Solution()

    result = solution.isPalindrome(head)

    print("Is Palindrome:", result)
