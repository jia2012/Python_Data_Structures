'''
Created on Sep 4, 2015

@author: shearora
'''

class MatchingBraces:
    
    def __init__(self):
        print("class initiated")
    
    def is_matched(self,exp):
        left = "{[("
        right = "}])"
        s = []
        if not exp:
            print ("expression is empty")
        else:
            for c in exp:
                if c in left:
                    s.append(c)
                    print ("c is in left")
                else:
                    if c in right:
                        print ("c is in right")
                        if not s:
                            return False
                        else:
                            s.pop()
        if not s:
            return True
        else:
            return False        
        
m = MatchingBraces()
print(m.is_matched("[][]")) 
       

