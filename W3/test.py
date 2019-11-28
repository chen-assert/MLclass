from math import log2
def cal(l,num):
    r=0
    for i in l:
        i.append(i[0]-i[1])
        r-=i[0]/num*(i[1]/i[0]*log2(i[1]/i[0])+i[2]/i[0]*log2(i[2]/i[0]))
    return r
height=-(3/8*(2/3*log2(2/3)+1/3*log2(1/3))+2/8*0+3/8*(2/3*log2(2/3)+1/3*log2(1/3)))
print(height)
he=[[3,2],[2,0.0000001],[3,2]]
bu=[[2,1],[3,2],[3,2]]
lo=[[5,3],[3,0.0000001]]
print(cal(he,8))
print(cal(bu,8))
print(cal(lo,8))