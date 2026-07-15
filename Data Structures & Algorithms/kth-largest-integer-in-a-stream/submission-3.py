class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)

        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        if self.heap and val < self.heap[0] and len(self.heap) == self.k:
            return self.heap[0]

        self.heap.append(val)
        heapq.heapify(self.heap)

        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        return self.heap[0]
