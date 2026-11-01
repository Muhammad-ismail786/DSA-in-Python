
class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        mp = {}

        for i, n in enumerate(nums):
            if n in mp:
                distance = abs(i - mp[n])

                if distance <= k:
                    return True

            mp[n] = i

        return False
