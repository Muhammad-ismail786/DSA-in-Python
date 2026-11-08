
def isAnagram(s, t):

    if len(s) != len(t):
        return False

    count = [0] * 26

    # Count characters in s
    for ch in s:
        count[ord(ch) - ord('a')] += 1

    # Decrease characters in t
    for ch in t:
        index = ord(ch) - ord('a')

        count[index] -= 1

        if count[index] < 0:
            return False

    return True


def main():

    s = input("Enter first string: ")
    t = input("Enter second string: ")

    if isAnagram(s, t):
        print("Output: True")
    else:
        print("Output: False")


if __name__ == "__main__":
    main()
