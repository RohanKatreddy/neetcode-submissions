class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        prefix_smallest = [-1] * len(heights)
        stack = []
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] >= h:
                stack.pop()
            
            if stack and heights[stack[-1]] < h:
                prefix_smallest[i] = stack[-1]
            
            stack.append(i)


        postfix_smallest = [len(heights)] * len(heights)
        heights_reversed = heights[::-1]
        stack = []
        for i, h in enumerate(heights_reversed):
            while stack and heights_reversed[stack[-1]] >= h:
                stack.pop()
            
            if stack and heights_reversed[stack[-1]] < h:
                postfix_smallest[i] = len(heights) - stack[-1] - 1
            
            stack.append(i)
        postfix_smallest.reverse()

        best = 0
        for i, h in enumerate(heights):
            volume = h * (postfix_smallest[i] - prefix_smallest[i] - 1)
            best = max(best, volume)
        
        return best