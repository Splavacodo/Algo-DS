class TimeMap:
    def __init__(self):
        self.key_vals = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.key_vals:
            self.key_vals[key].append((value, timestamp))
        else:
            self.key_vals[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        all_vals = self.key_vals.get(key, [])

        left = 0
        right = len(all_vals) - 1
        largest_timestamp = float("-inf")
        val_with_largest = ""

        while left <= right:
            mid = int((left + right) / 2)
            val_timestamp = all_vals[mid][1]

            if val_timestamp <= timestamp:
                largest_timestamp = max(largest_timestamp, val_timestamp)
                val_with_largest = all_vals[mid][0]
                left = mid + 1
            else:
                right = mid - 1
        
        return val_with_largest