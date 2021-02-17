class Solution(object):
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        if n == 0:
            return True

        i = 0
        j = n - 1

        while i <= j:

            while i < j and not self.isAscii(s[i].lower()):
                i += 1

            while i < j and not self.isAscii(s[j].lower()):
                j -= 1

            if s[i].lower() != s[j].lower():
                return False

            if j - i <= 1:
                return True

            i += 1
            j -= 1

        return False

    def isAscii(self, c):
        code = ord(c)
        if ord('a') <= code <= ord('z') or ord('A') <= code <= ord('Z') or ord('0') <= code <= ord('9'):
            return True

        return False


if True:
    o = Solution()
    s = "A man, a plan, a canal: Panama"

    res = o.isPalindrome(s)
    print("Result ", res)

if True:
    o = Solution()
    s = "race a car"

    res = o.isPalindrome(s)
    print("Result ", res)

if True:
    o = Solution()
    s = "0P"

    res = o.isPalindrome(s)
    print("Result ", res)

if True:
    o = Solution()
    s = ".,"

    res = o.isPalindrome(s)
    print("Result ", res)

if True:
    o = Solution()
    s = " "

    res = o.isPalindrome(s)
    print("Result ", res)
