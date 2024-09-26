# Create an empty stack
stack = []

# push items into the stack
def push(value):
    stack.append(value)
    print(f"Pushed:{value}")

# pop item from the stack
def pop():
    if is_empty():
        print("Stack is empty. Can't pop")
    else:
        item = stack.pop()
        print(f"Popped:{item}")

# check if the stack is empty
def is_empty():
    return len(stack) == 0

# peek at the top item of the stack
def peek():
    if is_empty():
        print("Stack is empty. Nothing in peek")
    else:
        print(f"Top item:{stack[-1]}")

push(10)
push(20)
push(30)

peek() # this should show 30
peek() # this should remove 30
peek() # this should show 20
