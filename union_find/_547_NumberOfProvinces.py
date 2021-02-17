from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * (n + 1)
        ans = 0

        for i in range(0, n):
            if self.dfs(i, isConnected, visited) > 0:
                ans += 1

        return ans

    def dfs(self, index, isConnected, visited):
        count = 0
        if visited[index]:
            return count

        visited[index] = True

        for i, v in enumerate(isConnected[index]):
            if v == 0:
                continue
            count += self.dfs(i, isConnected, visited)

        return count + 1


def runTestCase(fileName):
    f = open(fileName, 'r')

    isConnected = []

    arr = f.readline().strip()[2:-2].split('],[')
    for i in arr:
        isConnected.append(list(map(int, i.split(','))))

    s = Solution()
    res = s.findCircleNum(isConnected)
    print(res)

    f.close()


if True:
    runTestCase('../_in/union_find/_547_NumberOfProvinces_Sample1')

if True:
    runTestCase('../_in/union_find/_547_NumberOfProvinces_Sample2')
