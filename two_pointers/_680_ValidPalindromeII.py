class Solution(object):
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return self.isValid(l + 1, r, s) or self.isValid(l, r - 1, s)
            l += 1
            r -= 1

        return True

    def isValid(self, l, r, s: str):
        while l < r:
            if s[l] != s[r]:
                return False

            l += 1
            r -= 1

        return True


if True:
    o = Solution()
    s = "aba"

    res = o.validPalindrome(s)
    print("Result ", res)

if True:
    o = Solution()
    s = "abca"

    res = o.validPalindrome(s)
    print("Result ", res)

if True:
    o = Solution()
    s = "cbbcc"

    res = o.validPalindrome(s)
    print("Result ", res)

if True:
    o = Solution()
    s = "eccer"

    res = o.validPalindrome(s)
    print("Result ", res)

if True:
    o = Solution()
    s = "deeee"

    res = o.validPalindrome(s)
    print("Result ", res)

if True:
    o = Solution()
    s = "ebcbbececabbacecbbcbe"

    res = o.validPalindrome(s)
    print("Result ", res)
