from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for k, num in reversed(list(enumerate(digits))):
            if num < 9:
                digits[k] += 1
                return digits

            digits[k] = 0

        digits.insert(0, 1)
        return digits


if True:
    s = Solution()

    digits = [1, 2, 3]
    result = s.plusOne(digits)
    print("Result ", result)

if True:
    s = Solution()
    digits = [4, 3, 2, 1]
    result = s.plusOne(digits)
    print("Result ", result)

if True:
    s = Solution()
    digits = [9, 9, 9]
    result = s.plusOne(digits)
    print("Result ", result)

if True:
    s = Solution()
    digits = [1, 9, 9]
    result = s.plusOne(digits)
    print("Result ", result)
