class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(path, used):
            if len(path) == len(nums):
                res.append(path.copy())
                return

            for val in nums:
                if val not in used:
                    used.add(val)
                    path.append(val)
                    dfs(path, used)
                    used.remove(val)
                    path.pop()

        dfs([], set())
        return res