class Solution:
    def countAndSay(self, n: int) -> str:
        ans = "1"

        for k in range(1, n):
            i = 0
            tmp = str()

            while i < len(ans):
                j = i
                c = 0
                curr = ans[i]
                while j < len(ans) and ans[i] == ans[j]:
                    c += 1
                    j += 1

                tmp += str(c) + curr
                i = j if j > i else i + 1

            ans = tmp

        return ans


if True:
    o = Solution()
    n = 1

    res = o.countAndSay(n)
    print("Result ", res)

if True:
    o = Solution()
    n = 4

    res = o.countAndSay(n)
    print("Result ", res)

if True:
    o = Solution()
    n = 5

    res = o.countAndSay(n)
    print("Result ", res)
