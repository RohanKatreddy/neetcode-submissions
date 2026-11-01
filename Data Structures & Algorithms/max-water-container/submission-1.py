class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_volume = 0
        left_index = 0
        right_index = len(heights) - 1
        while(left_index < right_index):
            volume = min(heights[left_index], heights[right_index]) * (right_index - left_index)
            max_volume = max(max_volume, volume)
            if heights[right_index] < heights[left_index]: right_index -= 1
            else: left_index += 1
        
        return max_volume
