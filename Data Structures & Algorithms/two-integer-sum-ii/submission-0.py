class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_index = 0
        right_index = len(numbers) - 1

        while (left_index < right_index):
            two_sum = numbers[left_index] + numbers[right_index]
            if two_sum == target:
                return [left_index+1, right_index+1]
            if two_sum > target:
                right_index -= 1
            else:
                left_index += 1

        return [-1, -1]