class TimeMap:

    def __init__(self):
        self.d = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.d:
            self.d[key] = [[timestamp, value]]
        position = self._get_position(key, timestamp)
        lst = self.d[key]
        if position != -1 and lst[position][0] == timestamp:
                lst[position][1] = value        
        else:
            lst.insert(position+1, [timestamp, value])
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d: return ""
        position = self._get_position(key, timestamp)
        if position == -1: return ""
        return self.d[key][position][1]
        

    def _get_position(self, key, time):
        lst = self.d[key]
        left = 0
        right = len(lst) - 1
        ans = -1
        while left <= right:
            mid = (left + right)//2
            if lst[mid][0] <= time:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans