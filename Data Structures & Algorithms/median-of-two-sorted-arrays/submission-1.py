class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums2, nums1 = nums1, nums2
        length = (len(nums1) + len(nums2))
        start = 0
        end = len(nums1)
        while start <= end:
            partition1 = ((start + end)//2)
            partition2 = (length//2 - partition1)
            left1  = nums1[partition1 - 1] if partition1 > 0 else float('-inf')               # 2
            right1 = nums1[partition1]     if partition1 < len(nums1) else float('inf')
            left2  = nums2[partition2 - 1] if partition2 > 0 else float('-inf')
            right2 = nums2[partition2]     if partition2 < len(nums2) else float('inf')

            leastOnRightPartition = min(right1, right2)
            isValid = max(left1, left2) <= leastOnRightPartition

            if isValid:
                if length % 2 == 0:
                    return (max(left1, left2) + leastOnRightPartition)/2
                else:
                    return leastOnRightPartition
            
            if nums1[partition1] > leastOnRightPartition:
                end = partition1 - 1
            else:
                start = partition1 + 1

            