from collections import Counter 
def solve(A, B):
    N = len(B)
    K = len(A)

    MapA = Counter(A)
    need = len(MapA)
    MapB = {}
    ans = 0

    for i in range(K):
        if B[i] in MapA:
            if B[i] not in MapB:
                MapB[B[i]] = 1
            else:
                MapB[B[i]] += 1

            if MapB[B[i]] == MapA[B[i]]:
                need -= 1
                
    if need == 0: ans +=1

    left = 0
    right = K

    while right < N:
        if B[left] != B[right]:


            print("MapB",MapB,"need",need)

            if B[right] in MapA:
                if B[right] not in MapB:
                    MapB[B[right]] = 1
                else:
                    MapB[B[right]] += 1
                    
                if MapB[B[right]] == MapA[B[right]]:
                    need -= 1
                else:
                    need += 1


            if B[left] in MapB:
                MapB[B[left]] -= 1
                
                if MapB[B[left]] != MapA[B[left]]:
                    need += 1
                else:
                    need -= 1
                

                
        if MapB == MapA:
            ans += 1
        
        left += 1
        right += 1



    return ans 



A = "abc"
B = "abcbacabc"
# A = "aca"
# B = "acaa"

# A = "docp"
# B = "aoapeooeoapcpaocecddoocdcqqapeapccc"

A = "cbe"
B = "pbbqebdoecqboeepdcdbedaqacdopdaacaboqqocabdbeepdobdec"

print("solve",solve(A,B))