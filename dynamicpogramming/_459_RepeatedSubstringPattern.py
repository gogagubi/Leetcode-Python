class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        if n == 1:
            return False

        lps = [0] * n

        i = 0
        j = 1

        while j < n:
            if s[i] == s[j]:
                lps[j] = i + 1

                i += 1
                j += 1
            else:
                if i > 0:
                    i = lps[i - 1]
                else:
                    j += 1

        if lps[n - 1] == 0:
            return False

        patternLength = n - lps[n - 1]
        return True if n % patternLength == 0 else False


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
