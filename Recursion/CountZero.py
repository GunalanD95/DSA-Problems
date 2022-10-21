p1 = 120000005

class Solution:
    def CountZero(self,x):
        def revdigits(num,count):
            if num == 0:
                return count
            
            rem = num % 10
            if rem == 0:
                count += 1
                
            return revdigits(num//10,count)
            
         
        return revdigits(x,0)   
  
ll = Solution()  
print("Count",ll.CountZero(p1)) 
