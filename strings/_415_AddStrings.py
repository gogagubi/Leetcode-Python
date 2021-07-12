class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        ans = str()
        i = len(num1) - 1
        j = len(num2) - 1
        reminder = 0

        while i >= 0 or j >= 0 or reminder > 0:
            res = 0

            if i >= 0:
                res += int(num1[i])
                i -= 1

            if j >= 0:
                res += int(num2[j])
                j -= 1

            res += reminder
            reminder = res // 10

            ans = str((res % 10)) + ans

        return ans

if True:
    o = Solution()
    num1 = '23'
    num2 = '38'

    res = o.addStrings(num1, num2)
    print("Result ", res)

if True:
    o = Solution()
    num1 = '234'
    num2 = '11'

    res = o.addStrings(num1, num2)
    print("Result ", res)

if True:
    o = Solution()
    num1 = '378'
    num2 = '475'

    res = o.addStrings(num1, num2)
    print("Result ", res)
