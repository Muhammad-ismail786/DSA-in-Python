# 30. Substring with Concatenation of All Words

**LeetCode Problem:** [30. Substring with Concatenation of All Words](https://leetcode.com/problems/substring-with-concatenation-of-all-words/)

## # Intuition

We need to find all starting indices where the substring contains every word from the `words` array exactly once, in any order.

Since all words have the same length, we can use a Sliding Window and a Hash Map (`Counter`) to count words efficiently.

## # Approach

1. First, calculate the length of each word and the total number of words.
2. Create a `Counter` to store how many times each word appears in the `words` list.
3. Try different starting positions from `0` to `wordLength - 1`.
4. Use two pointers, `left` and `right`, to maintain a sliding window.
5. Extract a word of `wordLength` from the current `right` position.
6. If the extracted word does not exist in `wordCount`, clear the `seen` dictionary and reset the window.
7. If the word exists, increase its count in `seen`.
8. If a word appears more times than allowed, move the `left` pointer forward and remove extra words.
9. When the window contains all required words, add the `left` index to the answer.
10. Finally, return the answer list.

## # Complexity

- **Time complexity:** \(O(n \times m)\)

  Where `n` is the length of string `s` and `m` is the length of each word. This accounts for substring extraction and hash map operations.

- **Space complexity:** \(O(k \times m)\)

  Where `k` is the number of unique words and `m` is the length of each word.

## # Code

```python
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

        for i in range(wordLength):

            left = i
            count = 0

            seen = {}

            for right in range(i, len(s) - wordLength + 1, wordLength):

                word = s[right:right + wordLength]

                if word not in wordCount:
                    seen.clear()
                    count = 0
                    left = right + wordLength
                    continue

                seen[word] = seen.get(word, 0) + 1
                count += 1

                while seen[word] > wordCount[word]:

                    leftWord = s[left:left + wordLength]

                    seen[leftWord] -= 1
                    count -= 1

                    left += wordLength

                if count == totalWords:

                    ans.append(left)

                    leftWord = s[left:left + wordLength]

                    seen[leftWord] -= 1
                    count -= 1

                    left += wordLength

        return ans
```
