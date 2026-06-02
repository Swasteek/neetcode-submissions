class MyHashMap:

    def __init__(self):
        self.set=[[False,-1] for i in range(10000)]
        

    def put(self, key: int, value: int) -> None:
        curr=key%10000
        self.set[curr][0]=True
        self.set[curr][1]=value


    def get(self, key: int) -> int:
        curr=key%10000
        if self.set[curr][0]:
            return self.set[curr][1]
        return -1

    def remove(self, key: int) -> None:
        curr=key%10000
        self.set[curr][0]=False
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)