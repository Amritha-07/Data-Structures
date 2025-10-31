class Stack:
	def __init__(self):
		self.stack = []

	def push(self, element):
		self.stack.append(element)

	def pop(self):
		if(self.isEmpty()):
			return "Stack is Empty"
		return self.stack.pop()

	def peek(self):
		if(self.isEmpty()):
			return "Stack is Empty"
		return stack.stack[-1]

	def isEmpty(self):
		return True if len(self.stack) == 0 else False

	def size(self):
		return len(self.stack)

stack = Stack()
while(1):
	print("\n0.EXIT\n1.PUSH\n2.POP\n3.PEEK\n4.IS EMPTY\n5.SIZE")
	option = int(input("\nOPTION: "))
	if option == 0:
		break
	match option:
		case 1:
			element = int(input("\nELEMENT: "))
			stack.push(element)
		case 2:
			print(stack.pop())
		case 3:
			print(stack.peek())
		case 4:
			print(stack.isEmpty())
		case 5:
			print(stack.size())


