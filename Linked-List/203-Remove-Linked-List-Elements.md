
# 203. Remove Linked List Elements

## Intuition
We need to remove all nodes whose value equals `val` from the linked list.

## Approach
1. Remove matching nodes from the beginning of the list.
2. Set `current` to the updated head.
3. Traverse the remaining linked list.
4. If the next node's value equals `val`, skip that node.
5. Otherwise, move to the next node.
6. Return the updated head.

## Complexity

- **Time Complexity:** O(n), where n is the number of nodes.
- **Space Complexity:** O(1), because we use a constant amount of extra space.

## Code

```python
class Solution(object):
    def removeElements(self, head, val):
        while head is not None and head.val == val:
            head = head.next

        current = head

        while current is not None and current.next is not None:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next

        return head
```
