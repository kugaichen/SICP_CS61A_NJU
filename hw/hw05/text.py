result_list = ['A','C','D','E','F']
result = iter(result_list)
def odd(list):
    for x in list:
        yield x 
        
f = odd(result_list)
while 1:
    try:
        next(f)
    except:
        break
    
def sequence(start, step):
    while True:
        yield start
        start += step