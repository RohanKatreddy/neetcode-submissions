class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = {}
        for ch in s1:
            count[ch] = count.get(ch, 0) + 1

        left = 0
        for right, ch in enumerate(s2):
            count[ch] = count.get(ch, 0) - 1

            while min(count.values()) < 0:
                count[s2[left]] = count.get(s2[left], 0) + 1
                left += 1
            
            least = min(count.values())
            most = max(count.values())
            if least == most == 0:
                return True

        return False