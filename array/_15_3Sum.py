from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for k, i in enumerate(nums):
            if k == 0 or nums[k] != nums[k - 1]:
                left = k + 1
                right = len(nums) - 1

                while left < right:
                    sum = nums[k] + nums[left] + nums[right]
                    if sum == 0:
                        curr = [nums[k], nums[left], nums[right]]
                        result.append(curr)

                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1

                    if sum < 0:
                        left += 1
                    else:
                        right -= 1

        return result


if True:
    nums = [-1, 0, 1, 2, -1, -4]
    s = Solution()
    result = s.threeSum(nums)
    print("Result ", result)
