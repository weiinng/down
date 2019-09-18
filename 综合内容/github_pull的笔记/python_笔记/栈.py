# 先进后出 后进先出 

class Stack(object):

    def __init__(self):
        self.data = []

    def push(self,val):
        self.data.append(val)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

_stack = Stack()

_stack.push('佳俊')
_stack.push('咸鱼')

print(_stack.pop())
print(_stack.pop())