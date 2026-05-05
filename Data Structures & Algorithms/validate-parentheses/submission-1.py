class Solution:
    def isValid(self, s: str) -> bool:
        char_stack = []
        for c in s:
            if c in ['(', '{', '[']:
                char_stack.append(c)
            else:
                if len(char_stack) == 0 :
                    return False
                poped_char = char_stack.pop()
                if poped_char == '(' and c !=')':     
                    return False
                if poped_char == '{' and c != '}':
                    return False
                if poped_char == '[' and c != ']':
                    return False
        return len(char_stack) == 0                    