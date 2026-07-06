import heapq

class MedianFinder:

    def __init__(self):
        self.low = []   # max heap (negatives)
        self.high = []  # min heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.low, -num)

        # Move largest of low to high
        heapq.heappush(self.high, -heapq.heappop(self.low))

        # Keep low having >= high elements
        if len(self.high) > len(self.low):
            heapq.heappush(self.low, -heapq.heappop(self.high))

    def findMedian(self) -> float:
        if len(self.low) > len(self.high):
            return -self.low[0]
        return (-self.low[0] + self.high[0]) / 2