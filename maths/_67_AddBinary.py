class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = str()

        i = len(a) - 1
        j = len(b) - 1

        reminder = 0
        while i >= 0 or j >= 0 or reminder > 0:
            num = 0

            if i >= 0:
                num += int(a[i])
                i -= 1

            if j >= 0:
                num += int(b[j])
                j -= 1

            num += reminder

            ans = str(num % 2) + ans
            reminder = num // 2

        return ans


if True:
    s = Solution()
    a = "11"
    b = "1"
    res = s.addBinary(a, b)
    print("Result", res)

if True:
    s = Solution()
    a = "1010"
    b = "1011"
    res = s.addBinary(a, b)
    print("Result", res)

if True:
    s = Solution()
    a = "11"
    b = "11"
    res = s.addBinary(a, b)
    print("Result", res)
