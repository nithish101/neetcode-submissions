class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for i in range(len(nums))]
        freq = {}
        print(buckets)
        for num in nums:
            if num not in freq:
                freq[num] = 1
                buckets[0].append(num)
            else:
                freq[num] += 1
                buckets[freq[num] - 2].remove(num)
                buckets[freq[num] - 1].append(num)

        answer = []
        for i in range(len(buckets) - 1, -1, -1):
            if len(buckets[i]) > 0:
                for num in buckets[i]:
                    answer.append(num)
                    k -= 1
                    if k <= 0:
                        return answer

        return answer