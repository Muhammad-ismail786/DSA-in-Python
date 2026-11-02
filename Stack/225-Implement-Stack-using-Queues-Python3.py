
from collections import deque

class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        self.q2.append(x)

        while len(self.q1) > 0:
            value = self.q1.popleft()
            self.q2.append(value)

        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        return self.q1.popleft()

    def top(self) -> int:
        return self.q1[0]

    def empty(self) -> bool:
        return len(self.q1) == 0


# Example usage
obj = MyStack()

obj.push(1)
obj.push(2)
obj.push(3)

print(obj.top())    # 3
print(obj.pop())    # 3
print(obj.top())    # 2
print(obj.empty())  # False
