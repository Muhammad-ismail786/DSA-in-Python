# 23. Merge k Sorted Lists

**Difficulty:** Hard

**Topic:** Linked List, Heap, Priority Queue

**Languages:** Python, Python3

## Problem Description

You are given an array of `k` linked lists, where each linked list is sorted in ascending order.

Merge all the linked lists into one sorted linked list and return its head.

### Example

**Input:**

```text
lists = [
    1 -> 4 -> 5,
    1 -> 3 -> 4,
    2 -> 6
]
```

**Output:**

```text
1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6
```

## Intuition

We are given `k` sorted linked lists. We need to merge all of them into one sorted linked list.

Instead of comparing every node manually, we can use a Min Heap (`heapq`) to efficiently find the smallest available node.

Initially, we insert the first node of every non-empty linked list into the Min Heap.

The Min Heap always gives us the smallest node. We remove that node, attach it to our result list, and insert its next node into the heap.

We repeat this process until the heap becomes empty.

We also use a counter to handle nodes with equal values safely, without comparing the ListNode objects themselves.

## Approach

1. Import Python's `heapq` module.
2. Create an empty Min Heap.
3. Insert the first node of every non-empty linked list into the heap.
4. Use a counter to avoid comparing ListNode objects when node values are equal.
5. Create a dummy node to simplify building the merged linked list.
6. While the Min Heap is not empty:
   - Remove the smallest node using `heappop()`.
   - Attach it to the merged linked list.
   - Move the current pointer forward.
   - If the removed node has a next node, insert it into the heap using `heappush()`.
7. Return `dummy.next`, which is the head of the merged linked list.

## Complexity

- **Time Complexity:** O(N log k)
  - `N` is the total number of nodes across all linked lists.
  - `k` is the number of linked lists.
  - Every node is inserted into and removed from the heap once.

- **Space Complexity:** O(k)
  - The heap stores at most one available node from each linked list at a time.

## Code

```python
import heapq
from itertools import count


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:

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
```

## Key Concepts

| Concept | Meaning |
|---|---|
| `heapq` | Python module for heap operations |
| `heappush()` | Inserts an element into the heap |
| `heappop()` | Removes and returns the smallest element |
| `dummy` | Starting node used to build the result |
| `current` | Pointer to the last node in the result |
| `counter` | Prevents comparison of ListNode objects when values are equal |
