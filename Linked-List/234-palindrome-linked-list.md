# 234. Palindrome Linked List

## Intuition

We need to check whether a linked list reads the same forward and backward.

Example:

`1 -> 2 -> 2 -> 1`

This is a palindrome because the values are the same from both directions.

## Approach

1. Use two pointers, `slow` and `fast`, to find the middle of the linked list.
2. Reverse the second half of the linked list.
3. Compare the first half with the reversed second half.
4. If all corresponding values match, return `True`.
5. Otherwise, return `False`.

## Complexity

- **Time Complexity:** O(n) — We traverse the linked list to find the middle, reverse the second half, and compare values.
- **Space Complexity:** O(1) — We use only a few pointers and no extra data structure.

## Python 2 Code

```python
class Solution(object):
    def isPalindrome(self, head):
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow

        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        first = head
        second = prev

        while second is not None:
            if first.val != second.val:
                return False

            first = first.next
            second = second.next

        return True
```

## Python 3 Code

```python
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow

        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        first = head
        second = prev

        while second is not None:
            if first.val != second.val:
                return False

            first = first.next
            second = second.next

        return True
```
