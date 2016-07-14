import inspect
currVa = inspect.currentframe()

#######                 Sources                #######
strAll =    [
            '((((((((((((((0, 3)))))))))))))',
            '((((((((((((((1, 3)))))))))))})',
            '(([{(((((((((((2, 3)))))))))))))',
            '{(((((((((((((3, 3))))))))))))}',
            '({({(((]4)))})}',
            '((((5)))'
            ]

#######                 Work Siquece           #######
globDict= {'(':[[], [], ')', 'o'],
           ')':[[], [], '(', 'c'],
           '{':[[], [], '}', 'o'],
           '}':[[], [], '{', 'c'],
           '[':[[], [], ']', 'o'],
           ']':[[], [], '[', 'c'],
           'n':[[], [], ' ', ' ']
        }
#######     Chack symbol of parenthesis    #######
def checks(var):
    if  var == '(' or var == ')' or var == '{' or var == '}' or var == '[' or var == ']':
        return True
    else:
        return False
    #########        fill      #######
def fill(myDict, mySource):
    counterIncrement = 0
    counterDecrement = len(mySource)+1
    for item in mySource:
        counterIncrement += 1
        counterDecrement -= 1
        if checks(item):
            myDict[item][0].append(counterIncrement)
            myDict[item][1].append(counterDecrement)
        else:
            myDict['n'][0].append(counterIncrement)
            


#######                 Type of error             #######
def checkAmountParenthe(varDict):
    for parenthe in varDict:
        if checks(parenthe) and len(varDict[parenthe][0]) != len(varDict[varDict[parenthe][2]][1]) and varDict[parenthe][3] == 'o':
            print "erorr#1: in pairs parenthe, type is '{}{}'".format(parenthe,varDict[parenthe][2])
            
#*****************************************************************#                
def checkOrderParenthe(varDict, mySource):
    for parenthe in varDict:
        if checks(parenthe) and varDict[parenthe][3] == 'c':
            for position in varDict[parenthe][0]:
                #print 'MARKER!!! 1 !!!  {}   {}'.format(len(mySource)/2, position)
                if position <= len(mySource)/2+1 and position < varDict['n'][0][0]:
                    print "erorr#2: in order type parenthe, type is '{}'  position: {}".format(parenthe, position)
                          
#*****************************************************************#
def checkOrderParentheAmount(varDict, mySource):
    for parenthe in varDict:
        if checks(parenthe):
            tmpList = varDict[varDict[parenthe][2]][1][::-1]
            iteratorIncr = 0
            while iteratorIncr < len(mySource):                         #проверить "in" содержание по типу в листе антогониста
                #print(varDict[parenthe][0][iteratorIncr])
                if  len(varDict[parenthe][0]) > iteratorIncr and \      #   
                    len(tmpList) > iteratorIncr and \
                    (varDict[parenthe][0][iteratorIncr] not in tmpList or \
                    tmpList[iteratorIncr] not in varDict[parenthe][0]):
                    #varDict[parenthe][0][iteratorIncr] != tmpList[iteratorIncr]:
                    
                    print "erorr#3: parenthe type '{}' in position {} haven`t proper pair ".format(parenthe, varDict[parenthe][0][iteratorIncr])
                iteratorIncr += 1


#########        MAIN       ####### 
strNum = 5
#for strNum in range(0,len(strAll)):
print "parced strind @{}@".format(strAll[strNum])
fill(globDict,strAll[strNum])
checkAmountParenthe(globDict)
checkOrderParenthe(globDict,strAll[strNum])
checkOrderParentheAmount(globDict,strAll[strNum])
for i in globDict:
    print "{}  {}".format(i, globDict[i]) 


