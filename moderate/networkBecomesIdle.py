"""
2039. 网络空闲的时刻
"""
from typing import List
from collections import defaultdict
from collections import deque
inf = float('inf')


class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        n = len(patience)
        distance = [inf] * n
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        queue = deque([(0, 0)])
        distance[0] = 0
        while queue:
            server, cost = queue.popleft()
            distance[server] = cost
            for other in graph[server]:
                if distance[other] == inf:
                    distance[other] = cost + 1
                    queue.append((other, cost + 1))
        ans = 0
        for i in range(n):
            d, p = distance[i] * 2, patience[i]
            ans = max(ans, (d - 1) // p * p + d if p else 0)
        return ans + 1


edges = [[0, 1], [1, 2]]
patience = [0, 2, 1]  # res 8

obj = Solution()
res = obj.networkBecomesIdle(edges, patience)
print(res)
