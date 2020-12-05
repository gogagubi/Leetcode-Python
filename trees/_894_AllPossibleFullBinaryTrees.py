from model.treenode import TreeNode
from typing import List


class Solution:
    def allPossibleFBT1(self, N: int) -> List[TreeNode]:
        if N % 2 == 0:
            return []
        if N == 1:
            return [TreeNode(0)]

        res = []

        for L in range(1, N, 2):
            R = N - 1 - L
            L_list = self.allPossibleFBT(L)
            R_list = self.allPossibleFBT(R)

            for l_root in L_list:
                for r_root in R_list:
                    root = TreeNode(0)
                    root.left = l_root
                    root.right = r_root
                    res.append(root)

        return res

    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        result = []
        if N == 0:
            return result

        node = TreeNode(0)
        self.rec(result, node, node, N - 1)

        return result

    def rec(self, result, root, node, N):
        rootFlat = root.showFlatTree()
        node.left = TreeNode(0)
        node.right = TreeNode(0)

        if N - 2 == 0:
            rootFlat1 = root.showFlatTree()  # Just for demo purposes
            newTree = self.clone(root)
            result.append(newTree)
            node.left = None
            node.right = None
            rootFlat2 = root.showFlatTree()
            return


        self.rec(result, root, node.right, N - 2)

        self.rec(result, root, node.left, N - 2)

    def clone(self, tree: TreeNode) -> TreeNode:
        if not tree:
            return None
        new_tree = TreeNode(0)
        new_tree.left = self.clone(tree.left)
        new_tree.right = self.clone(tree.right)
        return new_tree


if True:
    s = Solution()
    N = 7
    res = s.allPossibleFBT(N)
    for i in res:
        print(i.showFlatTree())
