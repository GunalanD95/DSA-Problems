



def Pailndrome(S):
    def checkpalindrome(S,s,e):
        if s > e:
            print("Pailndrome")
            return
        
        if S[s] ==  S[e]:
            checkpalindrome(S,s+1,e-1)
        else:
            print("Not Pailndrome")



    checkpalindrome(S,0,len(S)-1)
    









if __name__ == '__main__':
    s = 'mom'
    print(Pailndrome(s))