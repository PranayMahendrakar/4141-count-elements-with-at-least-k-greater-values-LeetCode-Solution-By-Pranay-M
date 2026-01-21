class Solution:
    def countElements(self, nums: List[int], k: int) -> int:
        n = len(nums)
        sorted_nums = sorted(nums)
        count = 0
        
        for num in nums:
            # Count how many elements are strictly greater than num
            # Using binary search to find first element > num
            # Then count = n - that_position
            left, right = 0, n
            while left < right:
                mid = (left + right) // 2
                if sorted_nums[mid] <= num:
                    left = mid + 1
                else:
                    right = mid
            greater_count = n - left
            if greater_count >= k:
                count += 1
        
        return count