from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        result, curr, left, right = 0, 0, 0, len(height) - 1

        while left < right:
            minHeight = min(height[left], height[right])
            curr = minHeight * (right - left)
            result = max(curr, result)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return result


if True:
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    s = Solution()
    result = s.maxArea(height)
    print("Result ", result)
