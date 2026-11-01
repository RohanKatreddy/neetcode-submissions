class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dict = {}
        for i in t:
            dict[i] = dict.get(i, 0) + 1
        
        left = 0
        have = 0
        required = len(dict)
        best = float('inf')
        best_substr = [0, 0]
        for right, ch in enumerate(s):
            if ch in dict:
                dict[ch] -= 1
                if dict[ch] == 0:
                    have += 1

            while have == required:
                if right - left + 1 < best:
                    best = right - left + 1
                    best_substr = [left, right+1]

                out = s[left]
                if out in dict:
                    dict[out] += 1
                    if dict[out] == 1:
                        have -= 1
                left += 1

        
        return s[best_substr[0]:best_substr[1]]