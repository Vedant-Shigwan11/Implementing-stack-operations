class Stack:
    def __init__(self, limit=None):
        """Initialize the stack with an optional size limit."""
        self.stack = []
        self.limit = limit  # Maximum number of elements allowed in the stack

    def push(self, x):
        """Push an element onto the stack. Checks for stack overflow if a limit is set."""
        if self.limit is not None and len(self.stack) >= self.limit:
            print("Stack Overflow: Cannot push, stack is full.")
        else:
            self.stack.append(x)
            print(f"Pushed: {x}")

    def pop(self):
        """Remove and return the top element from the stack."""
        if not self.is_empty():
            popped_value = self.stack.pop()
            print(f"Popped: {popped_value}")
        else:
            print("Stack Underflow: Cannot pop, stack is empty.")

    def peek(self):
        """Return the top element without removing it."""
        if not self.is_empty():
            print(f"Top Element: {self.stack[-1]}")
        else:
            print("Stack is empty, nothing to peek.")

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.stack) == 0

    def size(self):
        """Return the current size of the stack."""
        print(f"Stack Size: {len(self.stack)}")

    def __str__(self):
        """Return a string representation of the stack."""
        if self.is_empty():
            return "Stack is empty."
        return "Stack (Top → Bottom): " + " -> ".join(map(str, reversed(self.stack)))

# Menu-Driven Program
def main():
    limit = int(input("Enter stack size limit (0 for no limit): "))
    limit = None if limit == 0 else limit  # Set limit to None if user enters 0
    my_stack = Stack(limit)

    while True:
        print("\nOptions:")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Check if stack is empty")
        print("5. Get stack size")
        print("6. Display stack")
        print("7. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            value = input("Enter value to push: ")
            my_stack.push(value)
        elif choice == '2':
            my_stack.pop()
        elif choice == '3':
            my_stack.peek()
        elif choice == '4':
            print("Stack is empty." if my_stack.is_empty() else "Stack is not empty.")
        elif choice == '5':
            my_stack.size()
        elif choice == '6':
            print(my_stack)
        elif choice == '7':
            print("Exiting program.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()


# OUTPUT: 
# Enter stack size limit (0 for no limit): 3

# Options:
# 1. Push
# 2. Pop
# 3. Peek
# 4. Check if stack is empty
# 5. Get stack size
# 6. Display stack
# 7. Exit
# Enter your choice: 1
# Enter value to push: 10
# Pushed: 10

# Enter your choice: 1
# Enter value to push: 20
# Pushed: 20

# Enter your choice: 6
# Stack (Top → Bottom): 20 -> 10

# Enter your choice: 3
# Top Element: 20

# Enter your choice: 2
# Popped: 20

# Enter your choice: 7
# Exiting program.
