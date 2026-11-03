class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []

        max_area = 0
        for current_index, height in enumerate(heights):
            temp = current_index
            while stack and stack[-1][1] > height:
                stack_index, stack_height = stack.pop()
                max_area = max(max_area, stack_height * (current_index - stack_index))
                temp = stack_index

            stack.append((temp, height))
        
        for index, height in stack:
            max_area = max(max_area, height * (len(heights) - index))
        
        return max_area