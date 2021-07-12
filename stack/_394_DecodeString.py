class Solution:
    def decodeString(self, s: str) -> str:
        ans = str()
        n = len(s)
        i = 0

        num = 0
        times = []
        chunks = []

        while i < n:
            if '0' <= s[i] <= '9':
                num = (num * 10) + (int(s[i]))
            elif s[i] == '[':
                times.append(num)
                num = 0

                chunks.append(ans)
                ans = str()
            elif s[i] == ']':
                tmp = chunks.pop()

                for _ in range(0, times.pop()):
                    tmp += ans

                ans = tmp
            else:
                ans += s[i]

            i += 1

        return ans


if True:
    o = Solution()
    s = "3[a]2[bc]"

    res = o.decodeString(s)
    print("Result ", res)

if True:
    o = Solution()
    s = "3[a2[c]]"

    res = o.decodeString(s)
    print("Result ", res)

if True:
    o = Solution()
    s = "2[abc]3[cd]ef"

    res = o.decodeString(s)
    print("Result ", res)

if True:
    o = Solution()
    s = "abc3[cd]xyz"

    res = o.decodeString(s)
    print("Result ", res)
