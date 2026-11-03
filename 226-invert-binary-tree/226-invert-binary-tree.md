# 226. Invert Binary Tree

## Intuition

The problem asks us to invert a binary tree by swapping the left and right children of every node.

We can use recursion to visit every node and swap its left and right children.

## Approach

1. Check if the root is `None`. If it is, return `None`.
2. Swap the left and right children of the current node.
3. Recursively invert the left subtree.
4. Recursively invert the right subtree.
5. Return the original root.

## Complexity

- **Time Complexity:** `O(n)` — Every node is visited exactly once.
- **Space Complexity:** `O(h)` — Recursion stack space depends on the height of the tree. In the worst case, it is `O(n)`.

## Code

See [226-invert-binary-tree.py](226-invert-binary-tree.py).

## Output

```text
Original Tree:
4 2 1 3 7 6 9

Inverted Tree:
4 7 9 6 2 3 1
```
