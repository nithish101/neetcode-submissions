class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-1 * stone for stone in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            a = heapq.heappop(stones)
            b = heapq.heappop(stones)
            if a == b:
                continue
            heapq.heappush(stones, a - b)
            print(stones)

        if len(stones) <= 0:
            return 0
        return -1 * stones[0]