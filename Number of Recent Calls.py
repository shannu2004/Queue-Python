from collections import deque
class RecentCounter:
    def __init__(self):
        self.requests=deque()
    def ping(self,t: int)-> int:
        self.requests.append(t)
        while self.requests[0]<t-3000:
            self.requests.popleft()
        return len(self.requests)

commands = ["RecentCounter", "ping", "ping", "ping", "ping"]
inputs = [[], [1], [100], [3001], [3002]]


counter = None
results = []

for command, inp in zip(commands, inputs):
    if command == "RecentCounter":
        counter = RecentCounter()
        results.append(None)  
    elif command == "ping":
        result = counter.ping(*inp)
        results.append(result)

print(results)
