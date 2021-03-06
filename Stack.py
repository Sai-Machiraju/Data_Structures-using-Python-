#creating Stack class()
 
 class Stack():
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    def is_empty(self):
        return self.items == []
    def get_stack(self):
        return self.items
        
#Integer number to Binary using Stack

    s=Stack()
    n=int(input())
    while n!=0:
        r=n%2
        n=n//2
        s.push(r)
    while not s.is_empty():
        print(s.pop(),end="")
 
#Checking whether Parenthesis are Balanced using Stack
     
        stack=Stack()
        if s=="":
            return True
        elif s[0] in ")]}" or len(s)==1:
            return False
        else:
            l=[i for i in s]
            for i in s:
                if i in "({[":
                    stack.push(i)
                    l.remove(i)
                else: 
                    if len(stack)!=0:
                        m=stack.pop()
                        if m+i in ["()","[]","{}"]:
                            pass
                        else:
                            return False
                    else:
                        return False
            if len(l)!=0 and len(stack)==0:   
                return True        
            else:
                return False
