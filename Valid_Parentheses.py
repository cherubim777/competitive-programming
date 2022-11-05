class Solution:
    def isValid(self, s: str) -> bool:
        compatibles = {'{': '}',
                       '[': ']',
                       '(': ')'
                     }
        
        stack=[]
        validity = None
        
        for i in s:
            if i in compatibles:
                stack.append(compatibles[i])
            else:
                try:
                    validity = i == stack.pop()
                except(IndexError):
                    validity = False
                finally:
                    if not validity:
                        break
                    
        return validity and len(stack) == 0
