# 2049.统计最高分数的节点数目
from typing import List


class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        # 节点数目
        n = len(parents)

        # children[i] 节点i的子节点
        children = [[] for _ in range(n)]
        for node, p in enumerate(parents):
            if p != -1:
                children[p].append(node)
        print(children)

        maxScore, cnt = 0, 0

        def dfs(node: int) -> int:
            score = 1
            size = n - 1
            for ch in children[node]:
                sz = dfs(ch)
                score *= sz
                size -= sz
            if node != 0:
                score *= size
            nonlocal maxScore, cnt
            if score == maxScore:
                cnt += 1
            elif score > maxScore:
                maxScore, cnt = score, 1
            return n - size
        dfs(0)
        return cnt


parents = [-1, 2, 0, 2, 0]
obj = Solution()
res = obj.countHighestScoreNodes(parents)
print(res)
