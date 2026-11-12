
class Solution(object):

    def isMatch(self, s, p):
        n = len(s)
        m = len(p)

        dp = [[-1] * (m + 1) for _ in range(n + 1)]

        def isMatchRec(n, m):

            if m == 0:
                return n == 0

            if dp[n][m] != -1:
                return dp[n][m]

            ans = False

            if p[m - 1] == '*':

                # Zero occurrences
                zero = isMatchRec(n, m - 2)

                # One or more occurrences
                oneOrMore = False

                if n > 0 and (p[m - 2] == s[n - 1] or p[m - 2] == '.'):

                    oneOrMore = isMatchRec(n - 1, m)

                ans = zero or oneOrMore

            else:

                if n > 0 and (s[n - 1] == p[m - 1] or p[m - 1] == '.'):

                    ans = isMatchRec(n - 1, m - 1)

            dp[n][m] = ans

            return ans

        return isMatchRec(n, m)


# Main function
if __name__ == "__main__":

    solution = Solution()

    s = input("Enter string: ")
    p = input("Enter pattern: ")

    result = solution.isMatch(s, p)

    print("Result:", result)
