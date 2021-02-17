from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        i = 0
        j = len(s) - 1

        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

        return s


if True:
    o = Solution()
    s = ["h", "e", "l", "l", "o"]

    res = o.reverseString(s)
    print("Result ", res)

if True:
    o = Solution()
    s = ["H", "a", "n", "n", "a", "h"]

    res = o.reverseString(s)
    print("Result ", res)
