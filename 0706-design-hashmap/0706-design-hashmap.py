from collections import deque

class MyHashMap:
    def __init__(self):
        self.hashmap = deque()  

    def put(self, key: int, value: int) -> None:
        for i in range(len(self.hashmap)):
            if self.hashmap[i][0] == key:
                self.hashmap[i][1] = value  
                return
        self.hashmap.append([key, value])  

    def get(self, key: int) -> int:
        for i in range(len(self.hashmap)):
            if self.hashmap[i][0] == key:
                return self.hashmap[i][1]
        return -1  

    def remove(self, key: int) -> None:
        for i in range(len(self.hashmap)):
            if self.hashmap[i][0] == key:
                self.hashmap.remove(self.hashmap[i])  
                return
