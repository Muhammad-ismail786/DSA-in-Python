# 205. Isomorphic Strings

## Intuition
We need to check whether characters in strings `s` and `t` follow the same pattern. Each character must consistently map to one character in the other string.

## Approach
1. If the lengths of both strings are different, return `False`.
2. Create two arrays, `map_s` and `map_t`, each containing 256 zeros.
3. Loop through both strings using index `i`.
4. Use `ord()` to convert each character into its numeric Unicode code point.
5. Compare the last-seen positions of the current characters. If they differ, return `False`.
6. Update both arrays with `i + 1` to record the current position.
7. If all characters follow the same pattern, return `True`.

## Complexity
- Time complexity: `O(n)`
- Space complexity: `O(1)` for the fixed-size arrays.

## Code

```python
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        map_s = [0] * 256
        map_t = [0] * 256

        for i in range(len(s)):
            if map_s[ord(s[i])] != map_t[ord(t[i])]:
                return False

            map_s[ord(s[i])] = i + 1
            map_t[ord(t[i])] = i + 1

        return True
```
