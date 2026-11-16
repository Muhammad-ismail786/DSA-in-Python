from collections import Counter
from typing import List


class Solution:

    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        ans = []

        if not words:
            return ans

        wordLength = len(words[0])
        totalWords = len(words)

        if len(s) < wordLength * totalWords:
            return ans

        wordCount = Counter(words)

        # Step 1: Try different starting positions
        for i in range(wordLength):

            left = i
            count = 0

            seen = {}

            # Step 2: Move through string
            for right in range(i, len(s) - wordLength + 1, wordLength):

                word = s[right:right + wordLength]

                # Step 3: Check if word exists
                if word not in wordCount:
                    seen.clear()
                    count = 0
                    left = right + wordLength
                    continue

                seen[word] = seen.get(word, 0) + 1
                count += 1

                # Step 4: Remove extra words
                while seen[word] > wordCount[word]:

                    leftWord = s[left:left + wordLength]

                    seen[leftWord] -= 1
                    count -= 1

                    left += wordLength

                # Step 5: All words found
                if count == totalWords:

                    ans.append(left)

                    leftWord = s[left:left + wordLength]

                    seen[leftWord] -= 1
                    count -= 1

                    left += wordLength

        return ans


if __name__ == "__main__":

    s = input("Enter string: ")

    n = int(input("Enter number of words: "))

    words = []

    print("Enter words:")

    for _ in range(n):
        words.append(input())

    obj = Solution()

    result = obj.findSubstring(s, words)

    print("Starting indices:", result)
