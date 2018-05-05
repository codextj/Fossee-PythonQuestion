import sys

def greaterThan(LHS,RHS):
    return LHS > RHS
 
def greaterThanEqsTo(LHS,RHS):
    return LHS >= RHS
 
def lessThan(LHS,RHS):
    return LHS < RHS
    
def lessThanEqsTo(LHS,RHS):
    return LHS <= RHS

def notEqsTo(LHS,RHS):
    return LHS != RHS
    
def eqsTo(LHS,RHS):
    return LHS == RHS

switcher = {
        '>': greaterThan,
        '>=': greaterThanEqsTo,
        '<': lessThan,
        '<=': lessThanEqsTo,
        '!=': notEqsTo,
        '=': eqsTo
    }
 

line_i =0
Score = 0
for line in sys.stdin:
    line_i += 1
    lcontent = line.strip("\n").split(' ')
    if(line_i > 2 and line_i < 13):
        a = int(lcontent[0])
        b = int(lcontent[2])
        Aops = lcontent[1] 
        Cops = lcontent[3]
        c = float(lcontent[4])
        
         
        if Aops == '*':
            ans = (a * b) 
        elif Aops == '/':
            ans = round((a / b),2) 
        elif Aops == '-':
            ans = (a - b) 
        elif Aops == '+':
            ans = (a + b) 
        else:
            print("Arithmetic Operation Exception")
        
        correctAns = switcher[Cops](ans,c)
        correctAns = str(correctAns)

        if lcontent[5] == correctAns:
            Score+=1
            
print(Score)


#I didn't knew there was this eval function in python which can solve this expressions in a snap 
#but since in our question we are asked to treat assignment operator('=') as a comparison operator(Equals To '==') which checks whether the LHS value is equals to RHS as it make sense for kids
#therefore In order to use eval function we need to replace '=' with '==' so that eval function can do equality check instead of assigning the value of RHS to LHS. 
#https://docs.python.org/3/library/functions.html#eval

