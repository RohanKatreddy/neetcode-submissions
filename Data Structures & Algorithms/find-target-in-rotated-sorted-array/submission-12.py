class Solution:
    def search(self, nums: List[int], target: int) -> int:
        k = len(nums) - 1
        if nums[0] > nums[-1]:
            k = 0
            step_size = len(nums)//2
            while step_size > 0:
                if k + step_size < len(nums) and nums[k + step_size] > nums[0]:
                    k += step_size
                else: step_size//=2
        
        start, end = 0, k + 1
        if nums[0] > target:
            start = k+1
            end = len(nums)
        if start >= end: return -1

        print(start, end)

        step_size = (end - start)//2
        while step_size > 0:
            if start + step_size < end and nums[start + step_size] <= target:
                start += step_size
            else: step_size //= 2
        
        return start if nums[start] == target else -1