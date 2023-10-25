class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None  # Return None when the stack is empty

    def is_empty(self):
        return len(self.items) == 0

    def __iter__(self):
        self.index = len(self.items) - 1
        return self

    def __next__(self):
        if self.index >= 0:
            element = self.items[self.index]
            self.index -= 1
            return element
        else:
            raise StopIteration

# Create a Stack object
stack = Stack()

# Push elements onto the stack
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

# Pop elements from the stack and print them in LIFO order using the iterator
print("Elements in LIFO order:")
for item in stack:
    print(item)

# Pop one more element and check if the stack is empty
popped_element = stack.pop()
if popped_element is not None:
    print(f"Popped element: {popped_element}")
else:
    print("Stack is empty.")
