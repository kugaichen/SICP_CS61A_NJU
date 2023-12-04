def xk(c, d):
    if c == 4:
         return 6
    elif d >= 4:
        return 6 + 7 + c
    else:
       return 25

def how_big(x):
    if x >10:
        print('huge')
    elif x>5:
        return 'big'
    elif x>0:
        print('small')
    else:
        print("nothin'")