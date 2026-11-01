class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Find the expected arrival time O(n)
        # Run nearest smallest elements
        expected_times = []
        cars = sorted(zip(position, speed), reverse=True)
        for i in range(len(cars)):
            expected_times.append((target-cars[i][0])/cars[i][1])
        
        stack = []
        for exp in expected_times:
            if not stack or stack[-1] < exp:
                stack.append(exp)

        return len(stack)