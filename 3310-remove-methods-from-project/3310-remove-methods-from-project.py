from collections import defaultdict

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:

        graph = defaultdict(list)

        for u, v in invocations:
            graph[u].append(v)

        suspicious = set()

        def dfs(node):
            if node in suspicious:
                return

            suspicious.add(node)

            for nei in graph[node]:
                dfs(nei)

        dfs(k)

        # Check if any outside node invokes a suspicious node
        for u, v in invocations:
            if u not in suspicious and v in suspicious:
                return list(range(n))

        # Remove suspicious methods
        ans = []

        for i in range(n):
            if i not in suspicious:
                ans.append(i)

        return ans