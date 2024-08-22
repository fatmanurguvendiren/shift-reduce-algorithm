def main():
    coordinat = ["0id", "0+", "0*", "0(","0)", "0$", "0E", "0T", "0F",
                 "1id", "1+","1*","1(",  "1)","1$","1E", "1T", "1F",
                 "2id", "2+", "2*", "2(","2)", "2$", "2E", "2T", "2F",
                 "3id", "3+", "3*", "3(", "3)", "3$", "3E", "3T", "3F",
                 "4id", "4+", "4*", "4(", "4)", "4$", "4E", "4T", "4F",
                 "5id", "5+", "5*", "5(", "5)", "5$", "5E", "5T", "5F",
                 "6id", "6+", "6*", "6(", "6)", "6$", "6E", "6T", "6F",
                 "7id", "7+", "7*", "7(", "7)", "7$", "7E", "7T", "7F",
                 "8id", "8+", "8*", "8(", "8)", "8$", "8E", "8T", "8F",
                 "9id", "9+", "9*", "9(", "9)", "9$", "9E", "9T", "9F",
                 "10id", "10+", "10*", "10(", "10)", "10$", "10E", "10T", "10F",
                 "11id", "11+", "11*", "11(", "11)", "11$", "11E", "11T", "11F"]

    values = ["S5","0","0","S4","0","0","1","2","3",
              "0","S6","0","0","0","accept","0","0","0",
              "0","R2","S7","0","R2","R2","0","0","0",
              "0","R4","R4","0","R4","R4","0","0","0",
              "S5","0","0","S4","0","0","8","2","3",
              "0","R6","R6","0","R6","R6","0","0","0",
              "S5","0","0","S4","0","0","0","9","3",
              "S5","0","0","S4","0","0","0","0","10",
              "0","S6","0","0","S11","0","0","0","0",
              "0","R1","S7","0","R1","R1","0","0","0",
              "0","R3","R3","0","R3","R3","0","0","0"
              ,"0","R5","R5","0","R5","R5","0","0","0"]

    inp = input("Enter your string: ")
    mystack = ["0"]
    inp = list(inp)
    myList = wanted(inp)
    myList.append ("$")
    ilkInput= str("0"+myList[0])
    starting = coordinat.index(ilkInput)
    action= values[starting]
    t = stack(action, mystack, myList, coordinat, values)

def wanted(myInput):
    while ("i" in myInput):
        indx = myInput.index(("i"))
        if myInput[indx + 1]:
            del myInput[indx + 1]
        myInput[indx] = "id"
    return myInput

def forReduce(l,ch):
    listInd=[]
    for i in range(1,len(l)):
        i -=1
        if (l[i]==ch):
            listInd.append(i)
    maxInd = max(listInd)
    return maxInd



def stack(action, mystack, newlist, coordinat, value):
    while (action != "accept"):
        if (action.startswith("S")):
            mystack += newlist[0]
            mystack.append(action[1:])
            del newlist[0]
            indx1 = coordinat.index(mystack[-1] + newlist[0])
            action = value[indx1]

            continue
        if (action.startswith("R")):
            mystack = list(mystack)
            reduceAction(action, mystack)
            index1 = coordinat.index(mystack[-2] + mystack[-1])
            action1 = value[index1]
            mystack.append(action1)
            index2 = coordinat.index(mystack[-1] + newlist[0])
            action = value[index2]


            continue
        if (action == '0'):
            print("INVALID string entered. SYNTAX ERROR!")
            break
    if (action == "accept"):
        print("VALID string entered. ACCEPTED!")


def reduceAction(action,mystack) :

    if (action == "R1"):
        #E -> E+T
        if("E" and "+" and "T" in mystack):
            indx = forReduce(mystack,"E")
            del mystack[indx+1:]

    if (action == "R2"):
        #E->T
        if("T" in mystack):
            indx = forReduce(mystack,"T")
            del mystack[indx+1:]
            mystack[indx]="E"

    if(action == "R3"):
        #T->T*F
        if("T" and "*" and "F" in mystack):
            indx = forReduce(mystack,"T")
            del mystack[indx+1:]
            mystack[indx] = "T"

    if(action == "R4"):
        #T->F
        if("F" in mystack):
            indx = forReduce(mystack,"F")
            del mystack[indx+1:]
            mystack[indx]="T"

    if(action == "R5"):
        #F->(E)
        if("E" and "(" and ")" in mystack):
            indx = forReduce(mystack,"(")
            del mystack[indx+1:]
            mystack[indx]="F"

    if(action == "R6"):
        #F->id
        if("i" in mystack):
            indx = forReduce(mystack,"i")
            del mystack[indx+1:]
            mystack[indx]="F"

    if (action == "Accept"):
        print("VALID string entered. ACCEPTED!")


main()
