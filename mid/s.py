def recursive(x,y):
    if y==0:
        return 1
    elif y>0:
        return x*recursive(x,y-1)
    else:
        return 1/recursive(x,-y)            


print(recursive(20,2))