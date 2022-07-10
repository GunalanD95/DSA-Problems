# Reverse a string using stacks and queues
from ListStack import stack


def reverse(string):

    # loop through the string and push each character to the stack
    # character by character onto the stack
    stk = stack()
    for i in string:
        stk.push(i)


    rs = ""
    while not stk.isEmpty():
        rs += stk.pop()
    return rs




print(reverse("crulgzfkif gg ombt vemmoxrgf qoddptokkz op xdq hv"))