class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left_index = 0
        right_index = 0
        visited = set()

        best = 0
        while (right_index < len(s)):
            while s[right_index] in visited:
                visited.remove(s[left_index])
                left_index += 1
            visited.add(s[right_index])

            best = max(best, len(visited))
            right_index += 1
        return best