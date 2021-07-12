class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        i = self.next(S, len(S) - 1)
        j = self.next(T, len(T) - 1)

        while i >= 0 and j >= 0 and S[i] == T[j]:
            i = self.next(S, i - 1)
            j = self.next(T, j - 1)

        return i == -1 and j == -1

    def next(self, s: str, i: int):
        skips = 0
        while i >= 0:
            if s[i] == '#':
                skips += 1
            elif skips > 0:
                skips -= 1
            else:
                return i
            i -= 1

        return -1


if True:
    o = Solution()
    S = "ab#c"
    T = "ad#c"

    res = o.backspaceCompare(S, T)
    print("Result ", res)

if True:
    o = Solution()
    S = "ab##"
    T = "c#d#"

    res = o.backspaceCompare(S, T)
    print("Result ", res)

if True:
    o = Solution()
    S = "a##c"
    T = "#a#c"

    res = o.backspaceCompare(S, T)
    print("Result ", res)

if True:
    o = Solution()
    S = "a#c"
    T = "b"

    res = o.backspaceCompare(S, T)
    print("Result ", res)

if True:
    o = Solution()
    S = "a#c"
    T = "a#cc"

    res = o.backspaceCompare(S, T)
    print("Result ", res)
