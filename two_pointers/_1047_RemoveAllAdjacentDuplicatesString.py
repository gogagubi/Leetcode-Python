class Solution(object):
    def removeDuplicates(self, S: str) -> str:
        n = len(S)
        j = 0
        arr = [' '] * n

        for i in range(0, n):
            if j > 0 and arr[j - 1] == S[i]:
                j -= 1
            else:
                arr[j] = S[i]
                j += 1

        return ''.join(arr[:j])


if True:
    o = Solution()
    S = 'abbaca'

    res = o.removeDuplicates(S)
    print("Result ", res)
