
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        # Always perform binary search on the smaller array
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        m = len(nums1)
        n = len(nums2)

        low = 0
        high = m

        while low <= high:

            # Find partition positions
            cut1 = low + (high - low) // 2
            cut2 = (m + n + 1) // 2 - cut1

            # Find boundary values of both arrays
            l1 = float('-inf') if cut1 == 0 else nums1[cut1 - 1]
            r1 = float('inf') if cut1 == m else nums1[cut1]

            l2 = float('-inf') if cut2 == 0 else nums2[cut2 - 1]
            r2 = float('inf') if cut2 == n else nums2[cut2]

            # Check if partition is correct
            if l1 <= r2 and l2 <= r1:

                # Even total number of elements
                if (m + n) % 2 == 0:
                    return (max(l1, l2) + min(r1, r2)) / 2.0

                # Odd total number of elements
                return max(l1, l2)

            # Move binary search towards left
            elif l1 > r2:
                high = cut1 - 1

            # Move binary search towards right
            else:
                low = cut1 + 1

        return 0.0


# Run the solution in VS Code
if __name__ == "__main__":

    solution = Solution()

    nums1 = [1, 3]
    nums2 = [2]

    result = solution.findMedianSortedArrays(nums1, nums2)

    print("Median:", result)
