# 25. Reverse Nodes in k-Group

**Difficulty:** Hard

**Topics:** Linked List, Recursion, Pointer Manipulation

**Languages:** Python, Python3

## Problem

Given the head of a linked list, reverse the nodes of the list `k` at a time.

If the number of remaining nodes is less than `k`, leave those nodes unchanged.

Only the nodes themselves may be changed, not their values.

## Example 1

**Input:**
```text
head = [1,2,3,4,5], k = 2
```

**Output:**
```text
[2,1,4,3,5]
```

**Explanation:**

The first two nodes are reversed, then the next two nodes are reversed. The last node remains unchanged.

## Example 2

**Input:**
```text
head = [1,2,3,4,5], k = 3
```

**Output:**
```text
[3,2,1,4,5]
```

**Explanation:**

The first three nodes are reversed. The remaining two nodes stay unchanged because they do not form a complete group of three.

## Intuition

We need to reverse the linked list in groups of `k` nodes.

We can solve this problem using recursion and three pointers.

Before reversing a group, we first check whether at least `k` nodes are available.

If fewer than `k` nodes remain, we return the list without reversing them.

## Approach

1. Initialize a temporary pointer `temp` with `head`.
2. Traverse `k` nodes to check whether a complete group is available.
3. If `temp` becomes `None`, return `head` because fewer than `k` nodes remain.
4. Initialize three pointers:
   - `prev = None`
   - `curr = head`
   - `next_node = None`
5. Reverse exactly `k` nodes using these three pointers.
6. Recursively call `reverseKGroup(curr, k)` to process the remaining nodes.
7. Connect the current reversed group's last node to the result of the recursive call.
8. Return `prev`, which points to the new head of the reversed group.

## Complexity

- **Time Complexity:** `O(n)` — Every node is visited a constant number of times.
- **Space Complexity:** `O(n/k)` — Recursive calls use stack space for each group. In the worst case, this becomes `O(n)` when `k = 1`.

## Python Code

```python
class Solution(object):
    def reverseKGroup(self, head, k):

        temp = head

        for i in range(k):
            if temp is None:
                return head

            temp = temp.next

        prev = None
        curr = head
        next_node = None

        for i in range(k):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        head.next = self.reverseKGroup(curr, k)

        return prev
```

## Python3 Code

```python
class Solution:
    def reverseKGroup(
        self,
        head: ListNode | None,
        k: int
    ) -> ListNode | None:

        temp = head

        for i in range(k):
            if temp is None:
                return head

            temp = temp.next

        prev = None
        curr = head
        next_node = None

        for i in range(k):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        head.next = self.reverseKGroup(curr, k)

        return prev
```

## Key Learning

- `temp` checks whether a complete group of `k` nodes exists.
- `prev` stores the previous node during reversal.
- `curr` points to the current node.
- `next_node` saves the next node before changing a link.
- Recursion processes the remaining groups.
- Only `next` pointers are changed; node values remain unchanged.
