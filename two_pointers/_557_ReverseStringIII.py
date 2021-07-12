class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)
        l = 0
        r = 0

        values = list(s)

        while r < n:
            while r < n and s[r] != ' ':
                r += 1

            k = r - 1
            while l < k:
                values[l], values[k] = values[k], values[l]
                l += 1
                k -= 1

            r += 1
            l = r

        return ''.join(values)


if True:
    o = Solution()
    s = "Let's take LeetCode contest"

    res = o.reverseWords(s)
    print("Result ", res)
