
# 44. Wildcard Matching

**Difficulty:** Hard

**Language:** Python / Python3

**Approach:** Greedy Algorithm

## Intuition

We need to check whether the given pattern `p` matches the entire string `s`.

There are two special characters:

- `?` matches any single character.
- `*` matches any sequence of characters, including an empty sequence.

We use a Greedy Approach to solve this problem.

We keep track of the last `*` position and use it to match additional characters whenever a mismatch occurs.

## Approach

1. Initialize two pointers `i` and `j` to traverse strings `s` and `p`.
2. Initialize `star = -1` to store the last position of `*`.
3. Initialize `match = 0` to store the position in string `s` where `*` starts matching.
4. If characters match or the pattern contains `?`, increment both pointers.
5. If the pattern contains `*`, save its position in `star` and the current string position in `match`.
6. If a mismatch occurs and a previous `*` exists, let `*` match one additional character and continue checking.
7. If no previous `*` exists, return `False`.
8. After processing the string, skip any remaining `*` characters in the pattern.
9. Return `True` if the entire pattern has been matched; otherwise, return `False`.

## Complexity

- **Time Complexity:** O(n + m) — The algorithm uses greedy matching with linear amortized time.
- **Space Complexity:** O(1) — Only a constant number of variables are used.

## Code

### Python

\`\`\`python
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        i = 0
        j = 0

        star = -1
        match = 0

        while i < len(s):

            if j < len(p) and (s[i] == p[j] or p[j] == '?'):

                i += 1
                j += 1

            elif j < len(p) and p[j] == '*':

                star = j
                match = i
                j += 1

            elif star != -1:

                j = star + 1
                match += 1
                i = match

            else:

                return False

        while j < len(p) and p[j] == '*':
            j += 1

        return j == len(p)


if __name__ == "__main__":

    s = input("Enter string: ")
    p = input("Enter pattern: ")

    obj = Solution()

    result = obj.isMatch(s, p)

    print("Output:", result)
\`\`\`

### Python3

\`\`\`python
class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        i = 0
        j = 0

        star = -1
        match = 0

        while i < len(s):

            if j < len(p) and (s[i] == p[j] or p[j] == '?'):

                i += 1
                j += 1

            elif j < len(p) and p[j] == '*':

                star = j
                match = i
                j += 1

            elif star != -1:

                j = star + 1
                match += 1
                i = match

            else:

                return False

        while j < len(p) and p[j] == '*':
            j += 1

        return j == len(p)


if __name__ == "__main__":

    s = input("Enter string: ")
    p = input("Enter pattern: ")

    obj = Solution()

    result = obj.isMatch(s, p)

    print("Output:", result)
\`\`\`
