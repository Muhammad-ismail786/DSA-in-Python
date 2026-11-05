# 231. Power of Two

## Intuition

A power of two is a number that can be divided by 2 repeatedly until it becomes 1.

Example:

16 → 8 → 4 → 2 → 1

If the final number becomes 1, it is a power of two.

## Approach

1. Check if n is less than or equal to 0. If yes, return False.
2. Use a while loop while n is completely divisible by 2.
3. Divide n by 2 in each iteration.
4. Finally, check whether n is equal to 1.
5. If n == 1, return True; otherwise, return False.

## Complexity

- **Time Complexity:** O(log n)
- **Space Complexity:** O(1)

## Python 3 Code

```python
def isPowerOfTwo(n):
    if n <= 0:
        return False

    while n % 2 == 0:
        n = n // 2

    return n == 1


n = 16
result = isPowerOfTwo(n)

print("Input:", n)
print("Is Power Of Two:", result)
```

## Example

Input: n = 16

Output: True

Explanation:

16 / 2 = 8

8 / 2 = 4

4 / 2 = 2

2 / 2 = 1

The final number is 1, so 16 is a power of two.
