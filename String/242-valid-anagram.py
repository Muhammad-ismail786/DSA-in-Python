
class Solution(object):
    def isAnagram(self, s, t):

        if len(s) != len(t):
            return False

        count = [0] * 26

        for ch in s:
            count[ord(ch) - ord('a')] += 1

        for ch in t:
            index = ord(ch) - ord('a')
            count[index] -= 1

            if count[index] < 0:
                return False

        return True


def main():

    s = input("Enter first string: ")
    t = input("Enter second string: ")

    solution = Solution()

    if solution.isAnagram(s, t):
        print("Output: True")
    else:
        print("Output: False")


if __name__ == "__main__":
    main()
