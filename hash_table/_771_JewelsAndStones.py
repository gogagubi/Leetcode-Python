class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ans = 0

        jewels_set = set()
        for i in jewels:
            jewels_set.add(i)

        for i in stones:
            if i in jewels_set:
                ans += 1
        return ans


if True:
    o = Solution()
    jewels = 'aA'
    stones = 'aAAbbbb'
    res = o.numJewelsInStones(jewels, stones)
    print(res)

if True:
    o = Solution()
    jewels = 'z'
    stones = 'ZZ'
    res = o.numJewelsInStones(jewels, stones)
    print(res)
