'''
Created on Jan 15, 2018

@author: arpit_jain2
'''

def tupleVarArgs(arg1, arg2='defaultB',*theRest):   #*theRest can cosume only non-keyword argumnet 
    """varaible argumnets"""
    print ('formal arg 1:', arg1)
    print ('formal arg 2:', arg2)
    print (theRest)                       #('xyz',456.789)
    for eachXtrArg in theRest:
        print ('another arg:', eachXtrArg) 
    print("Outside for ")
    
#calling functions        
tupleVarArgs('abc', 123, 'xyz', 456.789)       #this works       theRest = ('xyz', 456.789)
print ("----------------------------------------------------")
tupleVarArgs('abc', 123, [1,2,3],['A','b'])    #works    theRest =([1,2,3],['A','b'])
#tupleVarArgs('abc',123, arg4 = 'xyz')         #error
print ("----------------------------------------------------")
tupleVarArgs('abc')                            #this works *theRest tuple willbe empty

print ("----------------------------------------------------")

