
# LeetCode 32: Longest Valid Parentheses

## # Intuition

We are given a string containing only opening `(` and closing `)` parentheses.

We need to find the length of the longest valid parentheses substring.

We can solve this problem using a Stack.

Instead of storing parentheses, we store their indexes in the stack.

We initialize the stack with `-1` as the starting boundary.

## # Approach

1. Create a stack and initialize it with `-1`.
2. Initialize an answer variable with `0`.
3. Traverse the string using a loop.
4. If the current character is `(`, push its index into the stack.
5. Otherwise, pop the top index from the stack.
6. If the stack becomes empty, push the current index as a new boundary.
7. Otherwise, calculate the valid substring length using `i - stack[-1]`.
8. Update the maximum length using `max()`.
9. Return the final answer.

## # Complexity

- Time complexity: `O(n)`

  We traverse the string only once.

- Space complexity: `O(n)`

  In the worst case, the stack can store up to `n` indexes.

## # Python Code

```python
class Solution(object):

    def longestValidParentheses(self, s):
        stack = [-1]
        ans = 0

        for i in range(len(s)):

            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()

            if not stack:
                stack.append(i)
            else:
                ans = max(ans, i - stack[-1])

        return ans
```

## # Python3 Code

```python
class Solution:

    def longestValidParentheses(self, s: str) -> int:

        stack = [-1]
        ans = 0

        for i in range(len(s)):

            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()

            if not stack:
                stack.append(i)
            else:
                ans = max(ans, i - stack[-1])

        return ans
```
