class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 3
        
        first = []
        for i in range(n):
            first.append(-nums[i])

            
        heapq.heapify(first)
        total_sum = -sum(first)
        first_sum = [total_sum]
        for i in range(n, n*2):
            value = heapq.heappop(first)
            heapq.heappush(first, -nums[i])
            total_sum += nums[i] + value
            first_sum.append(total_sum)
        
        second = []
        for i in range(n*2, n*3):
            second.append(nums[i])
            
        heapq.heapify(second)
        total_sum = sum(second)
        second_sum = [total_sum]
        for i in range((n*2)-1, n-1, -1):
            value = heapq.heappop(second)
            heapq.heappush(second, nums[i])
            total_sum += nums[i] - value
            second_sum.append(total_sum)
            
        answer = sys.maxsize
        second_sum = second_sum[::-1]
        for i in range(n+1):
            answer = min(answer, first_sum[i] - second_sum[i])
            
        return answer