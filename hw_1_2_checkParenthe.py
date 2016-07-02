#######                 Sources                #######
str0 = '((((((((((((((2, 3)))))))))))))'
str1 = '((((((((((((((2, 3)))))))))))})'
str2 = '(([{(((((((((((2, 3)))))))))))))'
str3 = '{(((((((((((((2, 3))))))))))))}'
str4 = '(()3())'
#######                 Work Siquece           #######
globDict= {'(':[[], [],')'],')':[[], [],'('],
           '{':[[], [],'}'],'}':[[], [],'{'],
           '[':[[], [],']'],']':[[], [],'[']
       }
#######     Chack symbol of parenthesis    #######
def checks(var):
    if  var == '(' or var == ')' or var == '{' or var == '}' or var == '[' or var == '}':
        return True
    else:
        return False
#######                 Type of error             #######
def errMaker(varDict):
    for parenthe in varDict:
        print parenthe , varDict[parenthe]
        #for count in varDict[parenthe]:
         #   print varDict[parenthe][0], varDict[parenthe][1]

       #1 #if len(varDict[parenthe][0]) != len(varDict[varDict[parenthe][3]][0]) # erorr in pair parenthe
       


       #2#openParenthe = '({['
          #closeParenthe = ')}]'
          #if parenthe in openParenthe and varDict[varDict[parenthe][3]][1][0] > 

       #3 #if varDict[parenthe][0]) == varDict[varDict[parenthe][3]][0][::-1] # erorr in siquence parenthe
#########        fill      #######
def fill(myDict):
    counterIncrement = 0
    counterDecrement = len(str4)+1
    print len(str4)
    for item in str4:
        counterIncrement += 1
        counterDecrement -= 1        
        if checks(item):
            myDict[item][0].append(counterIncrement)
            myDict[item][1].append(counterDecrement)

   # print myDict
#########        MAIN       #######
fill(globDict)
errMaker(globDict)


