class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        para_dict = {')': '(', '}': '{', ']': '['}
        for par in s:
            if par not in para_dict:
                stack.append(par)
            elif stack and para_dict[par] == stack[-1]:
                stack.pop()
            else:
                return False
        if stack:
            return False
        return True