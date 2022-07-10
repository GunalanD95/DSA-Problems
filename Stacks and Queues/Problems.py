A = "(()"

A = "({)}"

A = '{([])}'

from ListStack import stack

l = '{(['
r = '])}'

ll = stack()


for i in range(len(A)):
    if A[i] in l:
        ll.push(A[i])

    elif A[i] in r:
        if len(ll.stk) == 0:
            print("0")

        top = ll.top()
        print("current top:", top)
        print("current char:", A[i])
        if top == '{' and A[i] == '}':
            ll.pop()

        elif top== '(' and A[i] == ')':
            ll.pop()
        
        elif top == '[' and A[i] == ']':
            ll.pop()

        else:
            print("Not Balanced")
            break


print("res",ll.getstack())