class MyQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x):
        self.s1.append(x)

    def pop(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())

        return self.s2.pop()

    def peek(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())

        return self.s2[-1]

    def empty(self):
        return not self.s1 and not self.s2


def main():
    my_queue = MyQueue()

    n = int(input("How many elements do you want to insert? "))

    for i in range(n):
        value = int(input(f"Enter element {i + 1}: "))
        my_queue.push(value)

    print("\nFront element:", my_queue.peek())
    print("Removed element:", my_queue.pop())

    if not my_queue.empty():
        print("Front element after Pop:", my_queue.peek())
    else:
        print("Queue is empty.")

    print("Is Queue empty?", my_queue.empty())


if __name__ == "__main__":
    main()
