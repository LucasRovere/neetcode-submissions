class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for num in nums:
            freq[num] -= 1

        num_freq = [(v, k) for k, v in freq.items()]
        heapq.heapify(num_freq)

        result = []
        for i in range(k):
            r = heapq.heappop(num_freq)
            result.append(r[1])

        return result[::-1]
        