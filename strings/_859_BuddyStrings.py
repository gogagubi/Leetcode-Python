class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        n = len(A)
        m = len(B)
        if n != m:
            return False

        if A == B:
            return len(set(A)) < n

        a = []
        b = []

        for i in range(0, n):
            if A[i] != B[i]:
                a.append(A[i])
                b.append(B[i])

        return len(a) == 2 and len(b) == 2 and a[0] == b[1] and a[1] == b[0]


if True:
    o = Solution()
    A = 'ab'
    B = 'ba'

    res = o.buddyStrings(A, B)
    print('Result ', res)

if True:
    o = Solution()
    A = 'ab'
    B = 'ab'

    res = o.buddyStrings(A, B)
    print('Result ', res)

if True:
    o = Solution()
    A = 'aa'
    B = 'aa'

    res = o.buddyStrings(A, B)
    print('Result ', res)

if True:
    o = Solution()
    A = 'abab'
    B = 'abab'

    res = o.buddyStrings(A, B)
    print('Result ', res)

if True:
    o = Solution()
    A = 'aaaaaaabc'
    B = 'aaaaaaacb'

    res = o.buddyStrings(A, B)
    print('Result ', res)

if True:
    o = Solution()
    A = 'abcd'
    B = 'badc'

    res = o.buddyStrings(A, B)
    print('Result ', res)