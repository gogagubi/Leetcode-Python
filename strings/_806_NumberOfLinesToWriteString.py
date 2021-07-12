from typing import List


class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        number_of_lines = 1
        last_line_width = 0

        n = len(s)

        for i in range(0, n):
            char_index = ord(s[i]) - ord('a')

            if last_line_width + widths[char_index] > 100:
                number_of_lines += 1
                last_line_width = 0

            last_line_width += widths[char_index]

        return [number_of_lines, last_line_width]


if True:
    o = Solution()
    widths = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    s = "abcdefghijklmnopqrstuvwxyz"

    res = o.numberOfLines(widths, s)
    print("Result ", res)

if True:
    o = Solution()
    widths = [4, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    s = "bbbcccdddaaa"

    res = o.numberOfLines(widths, s)
    print("Result ", res)
