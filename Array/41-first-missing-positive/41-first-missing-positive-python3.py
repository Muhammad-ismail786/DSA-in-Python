
class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:

        n = len(nums)

        for i in range(n):

            while (nums[i] >= 1 and
                   nums[i] <= n and
                   nums[nums[i] - 1] != nums[i]):

                correct_index = nums[i] - 1

                nums[i], nums[correct_index] = (
                    nums[correct_index], nums[i]
                )

        for i in range(n):

            if nums[i] != i + 1:
                return i + 1

        return n + 1


if __name__ == "__main__":

    solution = Solution()

    nums = [3, 4, -1, 1]

    result = solution.firstMissingPositive(nums)

    print("First Missing Positive:", result)
