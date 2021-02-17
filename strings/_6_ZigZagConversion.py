class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        arr = [str()] * numRows

        i = 0
        while i < n:
            j = 0
            while j < numRows and i < n:
                arr[j] += s[i]
                i += 1
                j += 1

            j = numRows - 2

            while j >= 1 and i < n:
                arr[j] += s[i]
                i += 1
                j -= 1

        ans = ''.join(i for i in arr)
        return ans


if True:
    o = Solution()
    s = "PAYPALISHIRING"
    numRows = 4

    res = o.convert(s, numRows)  # PINALSIGYAHRPI
    print("Result ", res)

if True:
    o = Solution()
    s = "AB"
    numRows = 1

    res = o.convert(s, numRows)  # AB
    print("Result ", res)
