# 42. Trapping Rain Water

**Difficulty:** Hard

**Topics:** Array, Two Pointers, Dynamic Programming, Stack

## Intuition

The problem asks us to calculate how much rainwater can be trapped between the bars.

Water can be trapped when there are taller bars on both the left and right sides of a position.

For each position, we consider:

- `leftMax`: Maximum height on the left side.
- `rightMax`: Maximum height on the right side.
- `height[i]`: Current bar height.

We use the Two Pointers approach to calculate the trapped water efficiently.

## Approach

1. Initialize two pointers:
   - `left = 0` points to the first element.
   - `right = len(height) - 1` points to the last element.

2. Initialize `leftMax` and `rightMax` to store the maximum heights found from both sides.

3. Initialize `water = 0` to store the total trapped rainwater.

4. Run a while loop while `left < right`.

5. Compare the heights at both pointers:
   - If `height[left] < height[right]`, process the left side.
   - Otherwise, process the right side.

6. For the left side:
   - Update `leftMax` if the current height is greater than or equal to it.
   - Otherwise, add `leftMax - height[left]` to `water`.
   - Move `left` forward.

7. For the right side:
   - Update `rightMax` if the current height is greater than or equal to it.
   - Otherwise, add `rightMax - height[right]` to `water`.
   - Move `right` backward.

8. Return the total trapped rainwater.

## Complexity

- **Time Complexity:** O(n)
  - Each pointer moves through the array at most once.

- **Space Complexity:** O(1)
  - Only a constant number of extra variables are used.

## Python Code

```python
def trap(height):

    left = 0
    right = len(height) - 1

    leftMax = 0
    rightMax = 0

    water = 0

    while left < right:

        if height[left] < height[right]:

            if height[left] >= leftMax:
                leftMax = height[left]
            else:
                water += leftMax - height[left]

            left += 1

        else:

            if height[right] >= rightMax:
                rightMax = height[right]
            else:
                water += rightMax - height[right]

            right -= 1

    return water
```

## Python3 Code

```python
class Solution:
    def trap(self, height: list[int]) -> int:

        left = 0
        right = len(height) - 1

        leftMax = 0
        rightMax = 0

        water = 0

        while left < right:

            if height[left] < height[right]:

                if height[left] >= leftMax:
                    leftMax = height[left]
                else:
                    water += leftMax - height[left]

                left += 1

            else:

                if height[right] >= rightMax:
                    rightMax = height[right]
                else:
                    water += rightMax - height[right]

                right -= 1

        return water
```

## Test Cases

**Example 1:**

Input:
```text
[0,1,0,2,1,0,1,3,2,1,2,1]
```

Output:
```text
6
```

**Example 2:**

Input:
```text
[4,2,0,3,2,5]
```

Output:
```text
9
```

**Example 3:**

Input:
```text
[3,0,2]
```

Output:
```text
2
```
