import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        my_stack = []
        my_set = {"+", "-", "*", "/"}

        ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv
        }

        for i in tokens:

            if i not in my_set:
                my_stack.append(int(i))

            else:
                first = my_stack.pop()
                second = my_stack.pop()

                if i == "/":
                    result = int(second / first)
                else:
                    result = ops[i](second, first)

                my_stack.append(result)

        return my_stack.pop()