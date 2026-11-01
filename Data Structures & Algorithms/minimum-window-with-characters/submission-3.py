class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dict = {}
        for i in t:
            dict[i] = dict.get(i, 0) + 1
        
        left = 0
        best = float('inf')
        best_substr = ""
        for right, ch in enumerate(s):
            if ch in dict: dict[ch] -= 1

            while max(dict.values()) <= 0:
                if s[left] in dict:
                    if dict[s[left]] < 0:
                        dict[s[left]] += 1
                        left += 1
                    else: break
                else: left += 1

            if max(dict.values()) <= 0:
                if (right - left + 1) < best:
                    best_substr = s[left:right+1]
                    best = right - left + 1
        
        return best_substr