import heapq


class Solution:
    def reorganizeString(self, S: str) -> str:
        ans = str()

        ascii = [0] * 127
        for i in S:
            ascii[ord(i)] -= 1

        max_heap = []
        for i in range(0, len(ascii)):
            if ascii[i] < 0:
                heapq.heappush(max_heap, (ascii[i], chr(i)))

        while len(max_heap) >= 2:
            curr = heapq.heappop(max_heap)
            next = heapq.heappop(max_heap)

            ans += curr[1]
            ans += next[1]

            if curr[0] < -1:
                heapq.heappush(max_heap, (curr[0] + 1, curr[1]))

            if next[0] < -1:
                heapq.heappush(max_heap, (next[0] + 1, next[1]))

        if len(max_heap) > 0:
            curr = heapq.heappop(max_heap)
            if curr[0] < -1:
                return ""

            ans += curr[1]

        return ans

if True:
    o = Solution()
    S = 'aab'
    res = o.reorganizeString(S)
    print(res)

if True:
    o = Solution()
    S = 'aaab'
    res = o.reorganizeString(S)
    print(res)

if True:
    o = Solution()
    S = 'aabac'
    res = o.reorganizeString(S)
    print(res)
