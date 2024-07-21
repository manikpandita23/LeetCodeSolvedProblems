from collections import defaultdict, deque
from typing import List
class Solution:
    def topologicalSort(self, k: int, conditions: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        in_degree = [0] * (k + 1)
        for u, v in conditions:
            graph[u].append(v)
            in_degree[v] += 1
        queue = deque([i for i in range(1, k + 1) if in_degree[i] == 0])
        topo_order = []
        while queue:
            node = queue.popleft()
            topo_order.append(node)
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        if len(topo_order) != k:
            return []
        return topo_order
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        row_order = self.topologicalSort(k, rowConditions)
        col_order = self.topologicalSort(k, colConditions)
        if not row_order or not col_order:
            return []
        row_pos = {num: i for i, num in enumerate(row_order)}
        col_pos = {num: i for i, num in enumerate(col_order)}
        matrix = [[0] * k for _ in range(k)]
        for num in range(1, k + 1):
            matrix[row_pos[num]][col_pos[num]] = num
        return matrix
sol = Solution()
k1 = 3
rowConditions1 = [[1, 2], [3, 2]]
colConditions1 = [[2, 1], [3, 2]]
print(sol.buildMatrix(k1, rowConditions1, colConditions1))
k2 = 3
rowConditions2 = [[1, 2], [2, 3], [3, 1], [2, 3]]
colConditions2 = [[2, 1]]
print(sol.buildMatrix(k2, rowConditions2, colConditions2))
