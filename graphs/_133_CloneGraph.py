from typing import List


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':

        def dfs(map: dict, node: Node):
            if node is None:
                return None

            if node.val in map:
                return map[node.val]

            newNode = Node(node.val, [])
            map[node.val] = newNode
            for neighbor in node.neighbors:
                newNode.neighbors.append(dfs(map, neighbor))

            return newNode

        map = {}
        return dfs(map, node)


if True:
    s = Solution()
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]
    res = s.cloneGraph(node1)
    print("Result", res.val)
