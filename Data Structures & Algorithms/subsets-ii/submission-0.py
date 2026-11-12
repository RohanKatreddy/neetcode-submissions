class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        
        def buildSolution(subset, k):
            if k == len(nums): return [subset.copy()]

            digit = nums[k]
            nxt = k
            while nxt < len(nums) and nums[nxt] == digit: nxt+=1
            numberOfDigits = nxt - k

            firstIteration = True
            result = []
            for multiplier in range(numberOfDigits+1):
                if not firstIteration:
                    subset.append(digit)
                firstIteration = False
                result.extend(buildSolution(subset, nxt))
            
            for _ in range(numberOfDigits):
                subset.pop()
            return result

        return buildSolution([], 0)