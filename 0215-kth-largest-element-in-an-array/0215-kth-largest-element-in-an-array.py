class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)
        for num in nums[k:]:
            if num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap,num)
        return heap[0]
        
        # quickselect ()time limit exceeded
        # k = len(nums)-k
        # def quickSelect(l,r):
        #     p, pivot = l, nums[r]
        #     for i in range(l,r):
        #         if nums[i] <= pivot:
        #             nums[i], nums[p] = nums[p], nums[i]
        #             p+=1
        #     nums[p], nums[r] = nums[r], nums[p]
        
        #     if p > k: return quickSelect(l,p-1)
        #     elif p < k: return quickSelect(p+1,r)
        #     else: return nums[p]
        # return quickSelect(0,len(nums)-1)