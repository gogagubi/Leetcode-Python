class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        num = 1

        while num < n:
            num *= 2

        return n == num


if True:
    s = Solution()
    n = 1
    res = s.isPowerOfTwo(n)
    print("Result", res)

if True:
    s = Solution()
    n = 16
    res = s.isPowerOfTwo(n)
    print("Result", res)

if True:
    s = Solution()
    n = 218
    res = s.isPowerOfTwo(n)
    print("Result", res)
