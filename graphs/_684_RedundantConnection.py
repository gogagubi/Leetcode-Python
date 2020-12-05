from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        res = []

        def find(parent, x):
            if parent[x] == x:
                return x
            return find(parent, parent[x])

        parent = []
        parent.extend(range(0, n + 1))

        for edge in edges:
            u = find(parent, edge[0])
            v = find(parent, edge[1])

            if u == v:
                res = edge
            else:
                parent[v] = u

        return res


if True:
    s = Solution()
    edges = [[1, 2], [1, 3], [2, 3]]
    res = s.findRedundantConnection(edges)
    print("Result", res)

if True:
    s = Solution()
    edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
    res = s.findRedundantConnection(edges)
    print("Result", res)
