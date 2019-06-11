class Solution:
    # @param A : string
    # @return an integer
    def braces(self, A):
        l=[]
        op=['+','-','*','/']
        flag=0
        for i in A:
            if i !=")":
                l.append(i)
            else:
                fl=0
                if i==")":
                    while l[-1] !="(":
                        if l[-1] in op:
                            fl=1
                        l.pop()
                    l.pop()
                    if fl==0:
                        return 1
                    if fl==1:
                        continue
                    if len(l)==0:
                        return 0            
            
                    if l[-1]=="(":
                        #l.pop()
                        return 1
                    
                    elif l[-1] not in op:
                        #l.pop()
                        return 1
                        
                        
        return 0
        
