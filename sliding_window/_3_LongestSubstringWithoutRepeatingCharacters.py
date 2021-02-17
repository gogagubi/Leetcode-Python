class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if s == 0:
            return 0

        m = {}

        i = 0
        j = 0

        ans = 0

        while i <= j < n:
            if not m.get(s[j], False):
                ans = max(ans, j - i + 1)

                m[s[j]] = True
                j += 1
            else:
                m[s[i]] = False
                i += 1

        return ans


if True:
    o = Solution()
    s = 'abcabcbb'

    res = o.lengthOfLongestSubstring(s)
    print("Result ", res)
