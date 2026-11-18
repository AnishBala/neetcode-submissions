import heapq
from collections import defaultdict
# Build a frequency dict — iterate through nums, count occurrences of each element.
# Push each (count, element) pair onto a min-heap.
# Cap heap size at k — if it exceeds k after a push, pop (evicts the smallest count).
# Extract the element from each remaining (count, element) pair in the heap and return as a list.
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for i in nums:
            freq[i] += 1
        
        heap = []
        for num, count in freq.items():
            heapq.heappush(heap, (count, num))

            if len(heap) > k:
                heapq.heappop(heap)

        result = []
        for count, num in heap:
            result.append(num)

        return result
                        
        

        