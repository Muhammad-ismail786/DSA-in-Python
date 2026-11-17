
class Solution(object):

    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """

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


if __name__ == "__main__":

    solution = Solution()

    s = input("Enter parentheses string: ")

    result = solution.longestValidParentheses(s)

    print("Longest Valid Parentheses Length:", result)
