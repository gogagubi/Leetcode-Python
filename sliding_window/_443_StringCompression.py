from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        l = 0
        r = 0
        k = 0

        while r < n:
            while r < n and chars[l] == chars[r]:
                r += 1

            chars[k] = chars[l]
            k += 1
            if r - l > 1:
                for i in str(r - l):
                    chars[k] = i
                    k += 1

            l = r

        return k


if True:
    o = Solution()
    chars = ['a', 'a', 'b', 'b', 'c', 'c', 'c']

    res = o.compress(chars)
    print('Result ', res)

if True:
    o = Solution()
    chars = ['a']

    res = o.compress(chars)
    print('Result ', res)

if True:
    o = Solution()
    chars = ['a', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']

    res = o.compress(chars)
    print('Result ', res)

if True:
    o = Solution()
    chars = ['a', 'a', 'a', 'b', 'b', 'a', 'a']

    res = o.compress(chars)
    print('Result ', res)
