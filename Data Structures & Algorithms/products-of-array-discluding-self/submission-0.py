class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1]
        for i in range(1, len(nums)+1):
            pre.append(pre[i-1] * nums[i-1])
        suf = [1]
        nums = nums[::-1]
        for i in range(1, len(nums)+1):
            suf.append(suf[i-1] * nums[i-1])
        output = []
        for i in range(1, len(nums)+1):
            output.append(pre[i-1] * suf[-i-1])
        return output