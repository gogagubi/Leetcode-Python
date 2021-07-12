class Solution:
    def helper(self, n, firstList, secondList):
        ans = ''
        i = 0
        j = 0

        for k in range(0, n):
            if k % 2 == 0:
                ans += firstList[i]
                i += 1
            else:
                ans += secondList[j]
                j += 1

        return ans

    def reformat(self, s: str) -> str:
        ans = ''

        n = len(s)
        alphas = list()
        numerics = list()

        for i in s:
            if i.isalpha():
                alphas.append(i)
            else:
                numerics.append(i)

        diff = abs(len(alphas) - len(numerics))
        if diff > 1:
            return ans

        if len(alphas) > len(numerics):
            ans = self.helper(n, alphas, numerics)
        else:
            ans = self.helper(n, numerics, alphas)

        return ans


if True:
    o = Solution()
    s = "a0b1c2"

    res = o.reformat(s)
    print("Result ", res)

if False:
    o = Solution()
    s = "leetcode"

    res = o.reformat(s)
    print("Result ", res)

if False:
    o = Solution()
    s = "1229857369"

    res = o.reformat(s)
    print("Result ", res)

if False:
    o = Solution()
    s = "covid2019"

    res = o.reformat(s)
    print("Result ", res)

if False:
    o = Solution()
    s = "ab123"

    res = o.reformat(s)
    print("Result ", res)
