
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


def main():
    stack = MyStack()

    stack.push(1)
    stack.push(2)
    stack.push(3)

    print("Top:", stack.top())

    print("Pop:", stack.pop())

    print("Top after pop:", stack.top())

    print("Is Empty:", stack.empty())

    stack.pop()
    stack.pop()

    print("Is Empty after removing all elements:", stack.empty())


if __name__ == "__main__":
    main()
