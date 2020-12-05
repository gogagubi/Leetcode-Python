from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for k, v in enumerate(nums):
            if target - v in map:
                return [k, map[target - v]]
            else:
                map[v] = k


# This is very slow solution, may because array operations
class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = [0, 0]
        for k, v in enumerate(nums):
            for k1, v1 in enumerate(nums[k + 1:], start=k + 1):
                if v + v1 == target:
                    return [k, k1]

        return result


if True:
    nums = [2, 7, 11, 15]
    s = Solution()
    target = 9
    result = s.twoSum(nums, 9)
    print("Result ", result)

if True:
    nums = [11, 15, 2, 7]
    s = Solution1()
    target = 9
    result = s.twoSum(nums, 9)
    print("Result ", result)
