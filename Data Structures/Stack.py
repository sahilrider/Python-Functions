class Stack(object):
	"""docstring for Stack"""
	def __init__(self,maxElem=50):
		super(Stack, self).__init__()
		self.top = -1
		self.maxElem = maxElem
		self.data = [None for i in range(50)]

	def push(self, value):
		if self.top == self.maxElem-1 :
			print("Stack Overflow")
			return

		self.top+=1
		self.data[self.top] = value

	def pop(self):

		if self.top == -1:
			print("Stack Underflow")
			return

		print("Popped Elem",self.data[self.top])
		self.top-=1

	def peek(self):
		if self.top == -1:
			print("Empty Stack")
			return None

		return self.data[self.top]

	def printStack(self):

		if self.top == -1:
			print("Empty Stack")
			return
		temp = self.top
		while(temp != -1):
			print(self.data[temp])
			temp-=1
		
if __name__ == '__main__':
	stack = Stack()
	stack.printStack()
	stack.pop()
	stack.push(1)
	stack.push(2)
	stack.push(3)
	stack.push(4)
	stack.push(5)
	stack.printStack()

	stack.pop()
	stack.printStack()
	print(stack.peek())
