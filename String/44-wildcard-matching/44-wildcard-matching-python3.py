
class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        i = 0
        j = 0

        star = -1
        match = 0

        while i < len(s):

            # Case 1: Characters match or '?' found
            if j < len(p) and (s[i] == p[j] or p[j] == '?'):

                i += 1
                j += 1

            # Case 2: '*' found
            elif j < len(p) and p[j] == '*':

                star = j
                match = i
                j += 1

            # Case 3: Previous '*' exists
            elif star != -1:

                j = star + 1
                match += 1
                i = match

            # Case 4: No match possible
            else:

                return False

        # Ignore remaining '*' characters
        while j < len(p) and p[j] == '*':
            j += 1

        return j == len(p)


if __name__ == "__main__":

    s = input("Enter string: ")
    p = input("Enter pattern: ")

    obj = Solution()

    result = obj.isMatch(s, p)

    print("Output:", result)
