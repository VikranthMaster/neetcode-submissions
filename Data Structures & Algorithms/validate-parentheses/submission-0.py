class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        someHash = {")":"(",
                    "]":"[",
                    "}":"{",
        }
        for x in s:
            if x in someHash:
                if stack and stack[-1] == someHash[x]:
                    stack.pop()
                else:
                    return False
            
            else:
                stack.append(x)
        
        return True if not stack else False

            