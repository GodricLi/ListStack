# _*_ coding=utf-8 _*_


class Stack(object):
    """
    使用列表实现栈
    """
    def __init__(self):
        self.stack = []

    def push(self, element):
        """
        添加元素进栈
        :param element:
        :return:
        """
        self.stack.append(element)

    def pop(self):
        """
        从栈取出元素
        :return:
        """
        return self.stack.pop()

    def get_top(self):
        """
        获取栈顶的元素
        :return:
        """
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.stack)
print(stack.pop())
print(stack.get_top())