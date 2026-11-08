
# 242. Valid Anagram

## Intuition

The main idea is to check whether both strings contain the same characters with the same frequency.

- If the lengths of both strings are different, return false.
- Create an array of size 26 to store character frequencies.
- Increase the frequency of each character in string `s`.
- Decrease the frequency of each character in string `t`.
- If any character's frequency becomes negative, return false.
- Otherwise, return true.

## Approach

1. First, check whether the lengths of both strings are equal.
2. Create a frequency array of size 26 initialized with zeros.
3. Traverse string `s` and increase the frequency of each character using `ord(ch) - ord('a')`.
4. Traverse string `t` and decrease the frequency of each character.
5. If any frequency becomes negative, return false.
6. If all characters are processed successfully, return true.

## Complexity

- Time complexity: O(n)

  We traverse both strings once, where n is the length of the strings.

- Space complexity: O(1)

  We use a fixed-size array of 26 elements.

## Python 2 Code

```python
def isAnagram(s, t):

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

    s = raw_input("Enter first string: ")
    t = raw_input("Enter second string: ")

    if isAnagram(s, t):
        print "Output: True"
    else:
        print "Output: False"


if __name__ == "__main__":
    main()
```

## Python 3 Code

```python
def isAnagram(s, t):

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

    if isAnagram(s, t):
        print("Output: True")
    else:
        print("Output: False")


if __name__ == "__main__":
    main()
```

## Example 1

Input:
```text
anagram
nagaram
```

Output:
```text
True
```

## Example 2

Input:
```text
rat
car
```

Output:
```text
False
```
