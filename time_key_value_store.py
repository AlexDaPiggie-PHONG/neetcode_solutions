class TimeMap:
    def __init__(self):
        self.store = {}
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = {}
        self.store[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store: return ""
        left, right = 1, len(self.store[key]) - 1
        print (f"DEBUG: len store = {len(self.store[key])}")
        result = ""
        while left <= right:
            mid = left + (right - left) // 2
            if mid == timestamp:
                print (f"DEBUG: the mid statement at the time checking is {mid}")
                return self.store[key][mid] 
            elif mid < timestamp: 
                result = self.store[key][mid]
                left = mid + 1
            else:
                right = mid - 1
        return result

input = ["TimeMap", "set", ["alice", "happy", 1], "get", \
         ["alice", 1], "get", ["alice", 2], "set", ["alice", "sad", 3], \
            "get", ["alice", 3]]

for i in range (len(input)): 
    if input[i] == "TimeMap":
        alex = TimeMap()
    if input[i] == "set":
        set_dict = input[i + 1]
        alex.set(set_dict[0], set_dict[1], set_dict[2])
        print (f"DEBUG: set = {alex.store}")
        i += 1
    if input[i] == "get":
        get_dict = input[i + 1]
        print (alex.get(get_dict[0], get_dict[1]))
    