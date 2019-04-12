def createstack():
    stack = []
    return stack

def push(stack, element):
    stack.append(element)

def pop(stack):
    return stack.pop()

stack = createstack()
push(stack,3)
push(stack,4)
push(stack,6)
print("After Push",stack)
pop(stack)
print("After Pop",stack)
