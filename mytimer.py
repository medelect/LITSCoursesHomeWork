
import time
reps = 1
repslist = range(reps)
'''memb "reps" numbers of repeat'''
def timer(func, *pargs, **kargs):
    '''func "timer" (func, *pargs, **kargs) handle function'''
    start = time.clock()
    for i in repslist:
        ret = func(*pargs, **kargs)
    elapsed = time.clock() - start
    return (elapsed, ret)