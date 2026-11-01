class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict = {}
        for char in s:
            if char in dict:
                dict[char] += 1
            else: dict[char] = 1
        for char in t:
            if char in dict:
                dict[char] -= 1
            else: return False
        for char in s:
            if dict[char] == 0:
                continue
            return False
        return True