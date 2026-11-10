# 2. Add Two Numbers

**LeetCode:** https://leetcode.com/problems/add-two-numbers/

**Difficulty:** Medium

**Topic:** Linked List

**Languages:** Python, Python3

## Intuition

We are given two numbers represented by two linked lists.

Each node contains one digit, and the digits are stored in reverse order.

We need to add both numbers and return the result as a linked list.

Example:

```text
l1 = 2 -> 4 -> 3
l2 = 5 -> 6 -> 4
```

These linked lists represent:

```text
342 + 465 = 807
```

Our answer will be:

```text
7 -> 0 -> 8
```

We use a `carry` variable to store the extra value when the sum is greater than or equal to 10.

## Approach

1. Create a dummy node to start the result linked list.
2. Create a current pointer to track the last node.
3. Initialize carry to 0.
4. Continue the loop while either linked list has nodes or carry is not zero.
5. Start total with the carry value.
6. If l1 is not None, add its value and move to the next node.
7. If l2 is not None, add its value and move to the next node.
8. If total is greater than or equal to 10, set carry to 1; otherwise, set it to 0.
9. Calculate the digit using `total % 10`.
10. Create a new node containing that digit.
11. Attach the new node to the result list.
12. Move current to the newly created node.
13. Return `dummy.next`.

## Example Dry Run

Input:

```text
l1 = 2 -> 4 -> 3
l2 = 5 -> 6 -> 4
```

| Round | l1 | l2 | Carry | Total | Digit |
|---|---:|---:|---:|---:|---:|
| 1 | 2 | 5 | 0 | 7 | 7 |
| 2 | 4 | 6 | 0 | 10 | 0 |
| 3 | 3 | 4 | 1 | 8 | 8 |

Output:

```text
7 -> 0 -> 8
```

## Complexity

**Time Complexity:** O(max(n, m))

We visit each node of both linked lists once.

**Space Complexity:** O(max(n, m))

We create a new linked list to store the result.

## Python LeetCode Code

```python
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
```

## Python3 LeetCode Code

```python
class Solution:
    def addTwoNumbers(
        self,
        l1: ListNode | None,
        l2: ListNode | None
    ) -> ListNode | None:

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
```
