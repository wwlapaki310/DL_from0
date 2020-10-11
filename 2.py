import numpy as np

def AND(x1,x2):
    x=np.array([x1,x2])
    w=np.array([0.5,0.5])
    b=-0.7
    tmp=np.sum(w*x)+b
    if tmp <=0:
        return 0
    elif tmp >0:
        return 1

def NAND(x1,x2):
    x=np.array([x1,x2])
    w=np.array([-0.5,-0.5])
    b=0.7
    tmp=np.sum(w*x)+b
    if tmp <=0:
        return 0
    elif tmp >0:
        return 1

def OR(x1,x2):
    x=np.array([x1,x2])
    w=np.array([0.5,0.5])
    b=-0.2
    tmp=np.sum(w*x)+b
    if tmp <=0:
        return 0
    elif tmp >0:
        return 1

def XOR(x1,x2):
    tmp_x1=OR(x1,x2)
    tmp_x2=NAND(x1,x2)
    y=AND(tmp_x1,tmp_x2)
    return y


for i in range(2):
    for j in range(2):
        print(XOR(i,j))