class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:

        result = []

        if len(nums) == 0:
            return result

        start = 0

        for i in range(1, len(nums)):

            if nums[i] != nums[i - 1] + 1:

                if start == i - 1:
                    result.append(str(nums[start]))
                else:
                    result.append(
                        str(nums[start]) + "->" + str(nums[i - 1])
                    )

                start = i

        if start == len(nums) - 1:
            result.append(str(nums[start]))
        else:
            result.append(
                str(nums[start]) + "->" + str(nums[-1])
            )

        return result


# Main function to test the solution
if __name__ == "__main__":
    obj = Solution()

    nums = [2, 3, 4, 7, 9, 10]

    result = obj.summaryRanges(nums)

    print(result)
