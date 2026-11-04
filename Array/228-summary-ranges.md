# 228. Summary Ranges – Python Solution

## Intuition

The main idea is to group consecutive numbers into ranges.

If numbers are consecutive, we keep them in the same range. If there is a gap, we finish the current range and start a new one.

For example:

Input:
```python
[2, 3, 4, 7, 9, 10]
```

Output:
```python
["2->4", "7", "9->10"]
```

## Approach

1. Create an empty list `result` to store the final ranges.
2. If the input list is empty, return the empty result.
3. Use `start = 0` to remember the starting index of the current range.
4. Start the loop from index `1` and compare the current number with the previous number.
5. If the current number is not consecutive with the previous number:
   - If the range contains only one number, append that number.
   - Otherwise, append the range in `"start->end"` format.
6. Update `start = i` to begin a new range.
7. After the loop, add the last range.
8. Return the result list.

## Complexity

- **Time Complexity:** O(n) – We traverse the list once.
- **Space Complexity:** O(n) – The result list stores the ranges. Auxiliary space is O(1), excluding the output.

## Code

```python
class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:

        result = []

        if len(nums) == 0:
            return result

        start = 0

        for i in range(1, len(nums)):

            if nums[i] != nums[i - 1] + 1:

                if start == i - 1:
                    result.append(str(nums[start]))
                else:
                    result.append(
                        str(nums[start]) + "->" + str(nums[i - 1])
                    )

                start = i

        if start == len(nums) - 1:
            result.append(str(nums[start]))
        else:
            result.append(
                str(nums[start]) + "->" + str(nums[-1])
            )

        return result
```
