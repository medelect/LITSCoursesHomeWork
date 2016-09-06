#!/usrbin/python

import __future__

GDH = {"stat": 1}

print("basicConsole application\n \
    created by Grutman Alex")

def baseInput():
    dataIn = raw_input(">>> ")
#    datain = input(">>> ")
    return dataIn.split(' ')

def funcArgIntParser(argList):
    funcArgumentsHash = {}
    argCounter = 0
    for item in argList:
        argCounter += 1
        item = item.split(' ')
        funcArgumentsHash[item[0]] = [argCounter, argList[-1]]
    

def typeParser(strList):
    print (strList)
    if strList[-1] == "int":
        GDH[strList[0]] = strList[2]
        print("int", strList[0], strList[2])
    elif strList[-1] == "list":
        strList[2] = strList[2].replace('(','')
        strList[-4] = strList[-4].replace(')','')
        GDH[strList[0]] = strList[2:-3]
        print("list", strList[0],strList[2:-3])
    elif len(strList) > 1 and strList[2] == "function":
        new = []
        tmp = strList[4:]
        tmp[0] = tmp[0].replace('(','')
        tmp[-1] = tmp[-1].replace(')','')
        tmp = " ".join(tmp)
        tmp = tmp.split(";")
        for i in tmp:
            i = i.strip(' ')
            new.append(i)
        GDH[strList[0]] = new
        print "function", strList[0], new

    else:
        print('uncnow command ', strList)
        return True
    return False

# fill choosed cells

while True:
    if typeParser(baseInput()):
        break

for j in GDH:
    print(j, GDH[j])
