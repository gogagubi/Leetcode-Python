class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return (s + s)[1:-1].find(s) != -1


if True:
    o = Solution()
    s = "abab"

    res = o.repeatedSubstringPattern(s)
    print("Result ", res)

if True:
    o = Solution()
    s = "aba"

    res = o.repeatedSubstringPattern(s)
    print("Result ", res)

if True:
    o = Solution()
    s = "abcabcabcabc"

    res = o.repeatedSubstringPattern(s)
    print("Result ", res)
