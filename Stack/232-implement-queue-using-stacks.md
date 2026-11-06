# 232. Implement Queue using Stacks

## Intuition

A Queue follows FIFO (First In, First Out), which means the element inserted first must be removed first.

A Stack follows LIFO (Last In, First Out), which means the last inserted element is removed first.

We can implement a Queue using two stacks (`s1` and `s2`).

- `s1` is used to insert new elements.
- `s2` is used to access and remove the front element.

When `s2` is empty, we transfer all elements from `s1` to `s2`. This reverses their order and gives us the correct FIFO behavior.

## Approach

1. **Push(x):**
   - Insert the element into `s1`.

2. **Pop():**
   - If `s2` is empty, transfer all elements from `s1` to `s2`.
   - Remove and return the top element of `s2`.

3. **Peek():**
   - If `s2` is empty, transfer all elements from `s1` to `s2`.
   - Return the top element of `s2` without removing it.

4. **Empty():**
   - Return true only when both stacks are empty.

## Complexity

- **Time complexity:**
  - Push: O(1) amortized
  - Pop: O(1) amortized
  - Peek: O(1) amortized
  - Empty: O(1)
  - Overall: O(n) for n operations.

- **Space complexity:** O(n), where n is the number of elements stored in the Queue.

## Python Code

See `232-implement-queue-using-stacks.py`.

## Python 3 Code

See `232-implement-queue-using-stacks-python3.py`.

## Example

**Input:**
```text
Push(10)
Push(20)
Push(30)
Peek()
Pop()
Peek()
Empty()
