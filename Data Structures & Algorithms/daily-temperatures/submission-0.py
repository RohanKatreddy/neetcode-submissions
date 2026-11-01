class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = []
        for i in range(1, len(temperatures)+1):
            val = temperatures[-i]
            if not stack:
                stack.append(i)
                output.append(0)
                continue

            while stack and temperatures[-stack[-1]] <= val:
                stack.pop()

            if not stack:
                stack.append(i)
                output.append(0)
            else:
                output.append(i - stack[-1])
                stack.append(i)
        
        return output[::-1]