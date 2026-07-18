# Find kth largest element in an array
nums = [3,2,1,5,6,4]
k = 2
import heapq
def KthLargest(nums, k):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]
print(KthLargest(nums, k))