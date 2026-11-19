# 41. First Missing Positive

## Intuition

We need to find the smallest positive integer that is missing from the given array.

We can solve this problem using the Cyclic Sort technique.

The idea is to place every valid positive number at its correct index.

For example:

- Number `1` should be at index `0`.
- Number `2` should be at index `1`.
- Number `3` should be at index `2`.
- Number `4` should be at index `3`.

After placing numbers at their correct positions, we traverse the array again.

If `nums[i]` is not equal to `i + 1`, then `i + 1` is the first missing positive integer.

## Approach

1. Get the length of the array and store it in `n`.
2. Traverse the array using a `for` loop.
3. Use a `while` loop to place each valid positive number at its correct index.
4. Check three conditions:
   - The number must be greater than or equal to `1`.
   - The number must be less than or equal to `n`.
   - The correct position must not already contain the same number.
5. Calculate the correct index using `nums[i] - 1`.
6. Swap the current number with the number at its correct position.
7. Traverse the array again.
8. If `nums[i] != i + 1`, return `i + 1`.
9. If all positions contain their correct numbers, return `n + 1`.

## Complexity

- Time complexity: $$O(n)$$

  Each valid number is moved to its correct position at most once. We traverse the array twice, so the overall time complexity is O(n).

- Space complexity: $$O(1)$$

  We rearrange the original array in place and use only a constant amount of extra space.

## Code

### Python

```python
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)

        for i in range(n):

            while (nums[i] >= 1 and
                   nums[i] <= n and
                   nums[nums[i] - 1] != nums[i]):

                correct_index = nums[i] - 1

                nums[i], nums[correct_index] = (
                    nums[correct_index], nums[i]
                )

        for i in range(n):

            if nums[i] != i + 1:
                return i + 1

        return n + 1
```

### Python3

```python
class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:

        n = len(nums)

        for i in range(n):

            while (nums[i] >= 1 and
                   nums[i] <= n and
                   nums[nums[i] - 1] != nums[i]):

                correct_index = nums[i] - 1

                nums[i], nums[correct_index] = (
                    nums[correct_index], nums[i]
                )

        for i in range(n):

            if nums[i] != i + 1:
                return i + 1

        return n + 1
```
