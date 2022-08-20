# Tower of Hanoi Problem

def TOH(n,src,dest,helper):

    # base condition 
    if n == 0:
        return 

    # MOVING N-1 DISCS FROM SOURCE TO HELPER USINF DESTINATION
    TOH(n-1,src,helper,dest)
    print("disk:",n,"src:",src,"dest:",dest)

    # MOVING N-1 HELPER FROM DESTINATION USING SOURCE
    TOH(n-1,helper,dest,src)



TOH(2,'1','3','2')



