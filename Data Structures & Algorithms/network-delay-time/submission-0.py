class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = [[] for i in range(n + 1)]

        for u, v, t in times:
            adj_list[u].append((v, t))
        visited = [False] * (n + 1)
        min_heap = [(0, k)]
        dist = {k:0}
        while min_heap:
            t, u = heapq.heappop(min_heap)
            if visited[u]:
                continue
            visited[u] = True
            for v, dt in adj_list[u]:
                if not visited[v]:
                    new_dist = t + dt
                    if v not in dist or new_dist < dist[v]:
                        dist[v] = new_dist
                    heapq.heappush(min_heap, (t + dt, v))
            
        return max(dist.values()) if len(dist) == n else -1