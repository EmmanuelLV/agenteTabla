
from random import randrange,randint,choice
import time
_actualState = randrange(0,8)

def q0():
    print("State Q0 ", end = '')
    time.sleep( 3 )
    _move = randint(1,2) # 1 - right, 2 - clean 
    if _move == 1:
        print("Moving to right (Q1)")
        q1()
    if _move == 2:
        print("Cleaning (Q5)")
        q4()
    else:
        print("0 - Estado inválido")

def q1():
    print("State Q1 ", end = '')
    time.sleep( 3 )
    _move = randint(1,2) # 0 - left, 1 - right, 2 - clean 
    if _move == 1:
        print("Moving to right (Q1)")
        q1()
    if _move == 2:
        print("Cleaning (Q3)")
        q3()
    else:
        print("1 - Estado inválido")

def q2():
    print("State Q2 ", end = '')
    time.sleep( 3 )
    _move = choice([0,1,2]) # 0 - left, 1 - right, 2 - clean 
    print(_move)
    if _move == 0:
        print("Moving to left (Q2)")
        q2()
    if _move == 1:
        print("Moving to right (Q1)")
        q2()
    if _move == 2:
        print("Cleaning (Q6)")
        q6()
    #if (_move != 1 or _move != 2 or _move != 3):
        # print("3Estado inválido")

def q3():
    print("State Q3 ", end = '')
    time.sleep( 3 )
    _move = randint(0,1) # 0 - left, 1 - right, 2 - clean 
    if _move == 0:
        print("Moving to left (Q2)")
        q2()
    if _move == 1:
        print("Moving to right (Q3)")
        q3()
    else:
        print("3 - Estado inválido")

def q4():
    print("State Q4 ", end = '')
    time.sleep( 3 )
    _move = randint(0,1) # 0 - left, 1 - right, 2 - clean 
    if _move == 0:
        print("Moving to left (Q2)")
        q4()
    if _move == 1:
        print("Moving to right (Q3)")
        q5()
    else:
        print("4 - Estado inválido")

def q5():
    print("State Q5 ", end = '')
    time.sleep( 3 )
    _move = choice([0,1,2]) # 0 - left, 1 - right, 2 - clean 
    if _move == 0:
        print("Moving to left (Q4)")
        q4()
    if _move == 1:
        print("Moving to right (Q5)")
        q5()
    if _move == 2:
        print("Cleaning (Q7)")
        q7()
    else:
        print("5 - Estado inválido")

def q6():
    print("State Q6 - End", end = '')
    """
    time.sleep( 3 )
    _move = randint(0,1)  # 0 - left, 1 - right, 2 - clean 
    if _move == 0:
        print("Moving to left (Q7)")
        q7()
    if _move == 1:
        print("Moving to right (Q4)")
        q6()
    else:
        print("Estado inasdválido")
    """
def q7():
    print("State Q7 - End ", end = '')

    """
    time.sleep( 3 )
    _move = randint(0,1) # 0 - left, 1 - right, 2 - clean 
    if _move == 0:
        print("Moving to left (Q6)")
        q6()
    if _move == 1:
        print("Moving to left (Q7)")
        q7()
    else:
        print("Estado inváasdlido")
"""

def Iniciar(_actualState):
    if _actualState == 0:
        q1()
    if _actualState == 1:
        q2()
    if _actualState == 2:
        q2()
    if _actualState == 3:
        q3()
    if _actualState == 4:
        q4()
    if _actualState == 5:
        q5()
    if _actualState == 6:
        q6()
    if _actualState == 7:
        q7()

Iniciar(_actualState)


