import random
import mytimer
name = 'SourseFile'
mode = 'a'

def genTor(_file,_action):
    f = open(_file, _action)
    tmp = ""
    for s in range(100000):
        for j in range(11):
            for i in range(8):
                tmp += chr(random.randint(97,110))
            tmp +=" "
        tmp +="\n"    
    f.write(tmp)
    f.close()

ret = mytimer.timer(genTor, name, mode)
print(ret[0])