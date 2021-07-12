class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        n = len(s)
        rev = True
        values = list(s)

        for i in range(0, n, k):
            if rev:
                l = i
                r = min(i + k - 1, n - 1)
                while l < r:
                    values[l], values[r] = values[r], values[l]
                    l += 1
                    r -= 1

            rev = not rev

        return ''.join(values)


if True:
    o = Solution()
    s = "abcdefg"
    k = 2

    res = o.reverseStr(s, k)  # bacdfeg
    print("Result ", res)

if True:
    o = Solution()
    s = "abcdef"
    k = 3

    res = o.reverseStr(s, k)  # cbadef
    print("Result ", res)

if True:
    o = Solution()
    s = "abcdefg"
    k = 8

    res = o.reverseStr(s, k)  # cbadef
    print("Result ", res)