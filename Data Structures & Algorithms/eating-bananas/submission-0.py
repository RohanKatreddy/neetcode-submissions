class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def calc_time(speed):
            total = 0
            for pile in piles:
                total += (-(-pile//speed))
            return total


        k = max(piles)
        step_size = k//2
        while step_size > 0:
            if k-step_size > 0 and calc_time(k - step_size) <= h:
                k -= step_size
            else: step_size//=2

        return k