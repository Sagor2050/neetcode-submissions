class Solution:
    def isValid(self, s: str) -> bool:

        left = {"(", "{", "["}

        my_dict = {")" : "(",
                   "}" : "{",
                   "]" : "[",}

        stack = []
        print(len(stack))

        for i in s:

            if i in left:
                stack.append(i)
                
            if i not in left:
                if not stack:
                    return False

                if stack.pop() != my_dict[i]:
                    return False
        print(len(stack))

        
        return len(stack) == 0

        