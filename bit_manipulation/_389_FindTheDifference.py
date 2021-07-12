class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        x = 0

        for i in s:
            x ^= ord(i)

        for i in t:
            x ^= ord(i)

        return chr(x)


if True:
    o = Solution()
    s = 'abcd'
    t = 'abcde'

    result = o.findTheDifference(s, t)
    print("Result ", result)

if True:
    o = Solution()
    s = ''
    t = 'y'

    result = o.findTheDifference(s, t)
    print("Result ", result)

if True:
    o = Solution()
    s = 'a'
    t = 'aa'

    result = o.findTheDifference(s, t)
    print("Result ", result)

if True:
    o = Solution()
    s = 'ae'
    t = 'aea'

    result = o.findTheDifference(s, t)
    print("Result ", result)
