class Solution:
    def trap(self, height: List[int]) -> int:
        biggest_left_tower = [0]
        biggest = height[0]
        for i in range(1, len(height)):
            biggest_left_tower.append(biggest)
            biggest = max(biggest, height[i])
        
        biggest_right_tower = [0]
        reversed_height = height[::-1]
        biggest = reversed_height[0]
        for i in range(1, len(height)):
            biggest_right_tower.append(biggest)
            biggest = max(biggest, reversed_height[i])
        biggest_right_tower = biggest_right_tower[::-1]
        

        volume = 0
        for i in range(len(height)):
            small_tower = min(biggest_left_tower[i], biggest_right_tower[i])
            if height[i] >= small_tower: continue
            volume += small_tower - height[i]

        return volume