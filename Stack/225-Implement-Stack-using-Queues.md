
# 225. Implement Stack using Queues

## Problem

Implement a Last-In-First-Out (LIFO) stack using only two queues.

The stack should support these operations:

- `push(x)`: Push element x onto the stack.
- `pop()`: Remove and return the top element.
- `top()`: Return the top element.
- `empty()`: Return true if the stack is empty.

## Intuition

A Stack follows LIFO (Last In, First Out).

This means the element inserted last will be removed first.

A Queue follows FIFO (First In, First Out).

This means the element inserted first will be removed first.

We use two queues (`q1` and `q2`) to make a queue behave like a stack.

Whenever we insert a new element:

1. Insert the new element into `q2`.
2. Move all elements from `q1` into `q2`.
3. Swap `q1` and `q2`.

After these steps, the newest element always stays at the front of `q1`.

## Approach

We use Python's `collections.deque` to implement both queues.

### 1. push(x)

- Insert the new element into `q2` using `append()`.
- Move all elements from `q1` to `q2` using `popleft()` and `append()`.
- Swap both queues using `q1, q2 = q2, q1`.

### 2. pop()

- Remove and return the front element of `q1` using `popleft()`.

### 3. top()

- Return the front element of `q1` using `q1[0]`.
- The element is not removed.

### 4. empty()

- Check whether `q1` is empty using `len(q1) == 0`.

## Complexity Analysis

| Operation | Time Complexity |
|---|---|
| push() | O(n) |
| pop() | O(1) |
| top() | O(1) |
| empty() | O(1) |

**Space Complexity:** O(n)

We use two queues to store the stack elements.

## Code (Python)

```python
from collections import deque


class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        self.q2.append(x)

        while len(self.q1) > 0:
            value = self.q1.popleft()
            self.q2.append(value)

        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        return self.q1.popleft()

    def top(self) -> int:
        return self.q1[0]

    def empty(self) -> bool:
        return len(self.q1) == 0
```
