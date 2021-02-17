from typing import List

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        pass


def runTestCase(fileName):
    f = open(fileName, 'r')

    accounts = []

    arr = f.readline().strip()[2:-2].split('], [')
    for i in arr:
        inList = []
        for j in i.split(", "):
            inList.append(j.replace('"', ''))
        accounts.append(inList)

    s = Solution()
    res = s.accountsMerge(accounts)
    print(res)

    f.close()


if True:
    runTestCase('../_in/union_find/_721_AccountsMerge_Sample1')
