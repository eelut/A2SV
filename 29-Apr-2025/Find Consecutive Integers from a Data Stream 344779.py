# Problem: Find Consecutive Integers from a Data Stream - https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/

class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.queue = deque(maxlen=self.k)

    def consec(self, num: int) -> bool:
        self.queue.append(num)
        while self.queue and self.queue[0] != num:
            self.queue.popleft()
        return len(self.queue) == self.k and self.queue[0] == self.value


        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)