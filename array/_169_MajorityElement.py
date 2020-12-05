from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        times = len(nums) // 2
        map = dict.fromkeys(nums, 0)

        for i in nums:
            map[i] += 1
            if map[i] > times:
                return i

        return -1


if True:
    s = Solution()
    nums = [3, 2, 3]
    result = s.majorityElement(nums)
    print("Result ", result)

if True:
    s = Solution()
    nums = [2, 2, 1, 1, 1, 2, 2]
    result = s.majorityElement(nums)
    print("Result ", result)
