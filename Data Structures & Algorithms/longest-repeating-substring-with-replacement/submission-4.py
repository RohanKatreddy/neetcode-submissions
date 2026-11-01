class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left_index = 0
        count = {}
        best = 0

        for right_index, ch in enumerate(s):
            
            if ch in count: count[ch] += 1
            else: count[ch] = 1

            while (right_index - left_index + 1 - max(count.values())) > k:
                count[s[left_index]] -= 1
                left_index += 1

            best = max(best, right_index - left_index + 1)

        return best