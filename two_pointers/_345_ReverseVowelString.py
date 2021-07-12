from typing import List


class Solution:
    def reverseVowels(self, s: str) -> str:
        l = list(s)

        i = 0
        j = len(l) - 1

        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

        while i < j:
            if l[i] not in vowels:
                i += 1
                continue

            if l[j] not in vowels:
                j -= 1
                continue

            l[i], l[j] = l[j], l[i]
            i += 1
            j -= 1

        return ''.join(l)


if True:
    o = Solution()
    s = "hello"

    res = o.reverseVowels(s)
    print("Result ", res)

if True:
    o = Solution()
    s = "leetcode"

    res = o.reverseVowels(s)
    print("Result ", res)
