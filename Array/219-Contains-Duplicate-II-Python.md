# 219. Contains Duplicate II

**Difficulty:** Easy
**Topics:** Array, Hash Table
**Language:** Python

## Intuition

We need to find whether the array contains two equal numbers whose index difference is less than or equal to `k`.

We can use a Python dictionary (`dict`) to store each number and its most recent index.

## Approach

1. Create an empty dictionary using `mp = {}`.
2. Traverse the array using `enumerate()`.
3. Check whether the current number already exists in the dictionary.
4. If it exists, calculate the difference between the current index and its previously stored index.
5. If the difference is less than or equal to `k`, return `True`.
6. Update the number's index in the dictionary.
7. If no valid pair is found, return `False`.

## Complexity

- **Time Complexity:** O(n) — We traverse the array once. Dictionary lookup and insertion take O(1) average time.
- **Space Complexity:** O(n) — The dictionary can store up to n different numbers.

## Code

```python
class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        mp = {}

        for i, n in enumerate(nums):
            if n in mp:
                distance = abs(i - mp[n])

                if distance <= k:
                    return True

            mp[n] = i

        return False
```

## Important Python Concepts

- `dict`: Python's built-in hash map.
- `mp = {}`: Creates an empty dictionary.
- `enumerate(nums)`: Provides both index and value while traversing a list.
- `n in mp`: Checks whether the number exists as a dictionary key.
- `mp[n]`: Retrieves the previously stored index.
- `abs()`: Calculates the absolute difference.
- `mp[n] = i`: Inserts or updates the number's latest index.
- `list[int]`: Type hint indicating a list of integers.
- `-> bool`: Indicates that the function returns a Boolean value.
