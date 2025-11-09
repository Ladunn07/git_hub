import math


def ptb1(a,b):
    if a==0 and b==0:
        return "INF"
    elif a==0 and b!=0:
        return "No.Solution"
    return -b/a
def ptb2(a,b,c):
    if a==0:
        return ptb1(b,c)
    else:
        delta=b**2-4*a*c
        if delta<0:
            return "No. Solution"
        elif delta==0:
            return "No. x1=x2={}".format(-b/(2*a))
        else:
            x1=(-b-math.sqrt(delta))/(2*a)
            x2 = (-b - math.sqrt(delta)) / (2 * a)
            return "x1={}, x2={}".format(x1,x2)
#test case1:
#0x^2+0x+0=0
print("0x^2+0x+0=0")
r=ptb2(0,0,0)
print(r)

#test case2:
#0x^2+0x+5=0
print("0x^2+0x+5=0")
r=ptb2(0,0,5)
print(r)

#test case3:
#0x^2+2x-5=0
print("0x^2+2x-5=0")
r=ptb2(0,2,-5)
print(r)

#test case4:
#1x^2-4x+4=0
print("1x^2-4x+4=0")
r=ptb2(1,-4,4)
print(r)