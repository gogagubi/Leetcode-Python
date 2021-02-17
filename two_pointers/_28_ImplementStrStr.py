class Solution(object):
    def strStr(self, haystack, needle):
        ans = 0
        n = len(haystack)
        m = len(needle)
        if m == 0:
            return ans

        ans = -1

        if n < m:
            return ans

        for i in range(0, n):
            for j in range(0, m):
                if i + j > n - 1 or haystack[i + j] != needle[j]:
                    break

                if j == m - 1:
                    return i

        return ans


if True:
    o = Solution()
    haystack = "hello"
    needle = "ll"

    res = o.strStr(haystack, needle)
    print("Result ", res)

if True:
    o = Solution()
    haystack = "aaaaa"
    needle = "bba"

    res = o.strStr(haystack, needle)
    print("Result ", res)

if True:
    o = Solution()
    haystack = ""
    needle = ""

    res = o.strStr(haystack, needle)
    print("Result ", res)

if True:
    o = Solution()
    haystack = "a"
    needle = "a"

    res = o.strStr(haystack, needle)
    print("Result ", res)

if True:
    o = Solution()
    haystack = "aaa"
    needle = "a"

    res = o.strStr(haystack, needle)
    print("Result ", res)
