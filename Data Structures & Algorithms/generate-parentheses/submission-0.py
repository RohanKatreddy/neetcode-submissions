class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def generateRecursively(s, openUsed, closedUsed):
            if len(s) == (2*n-1): return [s + ')']

            results = []
            if openUsed < n:
                results.extend(generateRecursively(s + '(', openUsed+1, closedUsed))
            
            closedLeft = n - closedUsed
            if closedLeft > 1 and closedUsed < openUsed:
                results.extend(generateRecursively(s + ')', openUsed, closedUsed + 1))

            return results

        return generateRecursively('', 0, 0)