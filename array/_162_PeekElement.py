from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        for k, v in enumerate(nums[:len(nums) - 1]):
            if v > nums[k + 1]:
                return k

        return len(nums) - 1


if True:
    s = Solution()
    nums = [1, 2, 3, 1]
    result = s.findPeakElement(nums)
    print("Result ", result)

if True:
    s = Solution()
    nums = [1, 2, 1, 3, 5, 6, 4]
    result = s.findPeakElement(nums)
    print("Result ", result)

if True:
    s = Solution()
    nums = [1, 2]
    result = s.findPeakElement(nums)
    print("Result ", result)

if True:
    s = Solution()
    nums = [-2147483648, -2147483647]
    result = s.findPeakElement(nums)
    print("Result ", result)
