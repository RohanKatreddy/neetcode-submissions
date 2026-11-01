class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left_index = 0
        right_index = 0
        count = {s[0]: 1}

        best = 0
        while right_index < len(s):
            
            best = max(best, right_index - left_index + 1)
            right_index += 1
            if right_index >= len(s): break

            key = s[right_index]
            if key in count: count[key] += 1
            else: count[key] = 1

            while (right_index - left_index + 1 - max(count.values())) > k:
                count[s[left_index]] -= 1
                left_index += 1

        return best