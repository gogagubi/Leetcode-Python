from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            res = res ^ i
        return res


if True:
    nums = [2, 2, 1]
    s = Solution()
    res = s.singleNumber(nums)
    print("Result ", res)

if True:
    nums = [4, 1, 2, 1, 2]
    s = Solution()
    res = s.singleNumber(nums)
    print("Result ", res)
