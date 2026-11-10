class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []


        def dfs(start, remain, path):
            if remain == 0:
                res.append(path.copy())
                return
            if start >= len(candidates) or candidates[start] > remain: return
            path.append(candidates[start])
            dfs(start + 1, remain - candidates[start], path)
            path.pop()

            next = start + 1
            while next < len(candidates) and candidates[next] == candidates[start]: next += 1
            dfs(next, remain, path)
            return

        dfs(0, target, [])
        return res