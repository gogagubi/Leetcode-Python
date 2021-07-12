class Solution:
    def longestPalindrome(self, s: str) -> int:
        ans = 0
        counts = [0] * 127

        for i in s:
            counts[ord(i)] += 1

        for i in counts:
            if i > 0:
                ans += (i // 2 * 2)
                if ans % 2 == 0 and i % 2 == 1:
                    ans += 1

        return ans


if True:
    o = Solution()
    s = "abccccdd"

    res = o.longestPalindrome(s)
    print("Result ", res)

if True:
    o = Solution()
    s = "a"

    res = o.longestPalindrome(s)
    print("Result ", res)

if True:
    o = Solution()
    s = "bb"

    res = o.longestPalindrome(s)
    print("Result ", res)

if True:
    o = Solution()
    s = "tattarrattat"

    res = o.longestPalindrome(s)
    print("Result ", res)

if True:
    o = Solution()
    s = "AAAAAA"

    res = o.longestPalindrome(s)
    print("Result ", res)

if True:
    o = Solution()
    s = "zeusnilemacaronimaisanitratetartinasiaminoracamelinsuez"

    res = o.longestPalindrome(s)
    print("Result ", res)
