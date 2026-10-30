# 206. Reverse Linked List

## Problem

Given the head of a singly linked list, reverse the list and return the new head.

## Intuition

We need to reverse the direction of every `next` pointer.

We use three variables:

- `prev`: Keeps the part of the list that has already been reversed.
- `current`: Points to the node we are currently processing.
- `next_node`: Temporarily saves the next node so we do not lose the remaining list.

Initially, `prev` is `None` because the reversed list is empty.

## Approach

Repeat these steps while `current` is not `None`:

1. Save the next node in `next_node`.
2. Point the current node's `next` to `prev`.
3. Move `prev` forward to the current node.
4. Move `current` forward to `next_node`.

When the loop finishes, `prev` points to the new head of the reversed list.

## Example

Original List:

`1 -> 2 -> 3 -> None`

Reversed List:

`3 -> 2 -> 1 -> None`

## Python Code

```python
class Solution:
    def reverseList(self, head):
        prev = None
        current = head

        while current:
            next_node = current.next

            current.next = prev

            prev = current
            current = next_node

        return prev
```

## Complexity Analysis

- **Time Complexity: O(n)**
  - Each node is visited exactly once.

- **Space Complexity: O(1)**
  - Only a fixed number of variables are used.
  - Existing nodes are rearranged without creating another list.

## Important Python Concepts

- `None`: Represents the absence of a value.
- `current`: A variable that holds the current linked-list node.
- `current.next`: Accesses the next node.
- `next_node`: Temporarily stores the next node.
- `while current`: Continues the loop until current becomes None.
- `return prev`: Returns the new head of the reversed list.
- References: Variables hold references to existing nodes, allowing us to change their links.

## GitHub

```bash
git add src/Linked-List/206-Reverse-Linked-List.md
git commit -m "Add Reverse Linked List explanation in Python"
git push origin main
```

```bash
git add src/Linked-List/206-Reverse-Linked-List.py
git commit -m "Add Reverse Linked List solution in Python"
git push origin main
```
