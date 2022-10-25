# skip a string 
st = 'abbcdde'
st = list(st)
skip = 'b'

def skipstring(st,indx,skip):
    ans = []
    if indx == len(st):
        return ans
    
    if st[indx] != skip:
        ans.append(st[indx])
        
    return_val = skipstring(st,indx+1,skip)
    
    if return_val:
        ans.extend(return_val)
    
    return ans 
print("Skip",skipstring(st,0,skip))