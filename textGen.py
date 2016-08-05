import random

f = open('SourseFile', 'w')
tmp = ""
for s in range(100000):
    for j in range(11):
        for i in range(8):
            tmp += chr(random.randint(97,110))
        tmp +=" "
    tmp +="\n"    
f.write(tmp)
f.close()