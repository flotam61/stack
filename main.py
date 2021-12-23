
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

def check(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()

        index = index + 1

    if balanced and s.isEmpty():
        print('Сбалансированно')
        return True
    else:
        print('Несбалансированно')
        return False

print(check('((()))'))
print(check('(((('))


# s = Stack()
# t = Stack()
# s.push('hi')
# s.push('priv')
# print(s.size())
# s.pop()
# print(s.items)