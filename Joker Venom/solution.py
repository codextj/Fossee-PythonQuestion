pin,currentPos,time = map(str,input().split(' '))
time = int(time)
totalTurns = 0
doorPwd = ''
afterRotationStates = [] 

def getMinAndPrintInstructions(targetDigit,targetDigitIndex,currentDigit):
    #print('to get',targetDigit,'from',currentDigit)
    if targetDigit == currentDigit:
        print('already set')
        turnThisDialBy = 0
    else:
        rotateLeftBy  = targetDigitIndex 
        rotateRightBy = (9-targetDigitIndex) +1
        
        if rotateLeftBy < rotateRightBy:
            turnThisDialBy = rotateLeftBy
            print('rotate dial towards left by '+str(turnThisDialBy))
        elif rotateLeftBy > rotateRightBy:
            turnThisDialBy = rotateRightBy
            print('rotate dial towards right by '+str(turnThisDialBy))
        else:
            turnThisDialBy = rotateLeftBy # or rotateRightBy 
            print('rotate dial in any direction by '+str(turnThisDialBy))
        
    return turnThisDialBy  

                
numberPattern = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(4):
    targetDgt = int(pin[i])
    currentDgt = int(currentPos[i])
    currentDgtConfig = numberPattern[currentDgt:]+numberPattern[:currentDgt]
    #[|'3'|, '4', '5', '6', '7', '8', {'9'}, '0', '1', '2'] 
    
    targetDgtIndex = currentDgtConfig.index(targetDgt)
    turnThisDialBy = getMinAndPrintInstructions(targetDgt,targetDgtIndex,currentDgt) 
    
    doorPwd+= str(turnThisDialBy)
    totalTurns += turnThisDialBy

    
    
print(str(totalTurns*time)+' milliseconds\nDoor lock key '+doorPwd)

totalTurnsDl =0
currentConfig,timeDl = map(str,input().split(' '))
spzlNumPattern = input().split(' ')
for i in range(4):
    
    trgDigit = doorPwd[i]
    
    curDigt  = currentConfig[i]
    config = spzlNumPattern[spzlNumPattern.index(curDigt):] + spzlNumPattern[:spzlNumPattern.index(curDigt)]
    
    trgDigitIndex = config.index(trgDigit)
    totalTurnsDl += getMinAndPrintInstructions(trgDigit,trgDigitIndex,curDigt)
    
    print(*(config[trgDigitIndex:]+config[:trgDigitIndex])) #after rotation

print(str(totalTurnsDl*time)+' milliseconds')
