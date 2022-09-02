'''
Do the following, then show and explain them to the TA:

1. In the Content section here in LearningSuite, 
find the sample code #1 and copy it into the script editor in Maya. 
Play around with it. Try to figure out how variables work, 
then explain what the code is doing. Add code that takes in 
a number from a prompt then adds that number to your bank account amount and prints the new number.
'''

#1 
# Example 1
num1 = 2
num2 = 5
num3 = 10
total = num1 + num2 + num3
print("First total")
print(total)

num2 = 8
stringToPrint = "Next total"
print(stringToPrint)
print(total)

total = total + num2
print( "Now total = " + str(total) )

numList = [2, 4, 6, 8]
print(numList[0])
print(numList[3])

product = numList[0] * numList[1]
anotherStringToPrint = "The current product is " + str(product)
print(anotherStringToPrint)

product = product * numList[2]
product = product * numList[3]
print( "Product = " + str(product) )

paycheck1 = 280.79
paycheck2 = 590
bankAmount = paycheck1 + paycheck2       # this is how many dollars is in your bank account!
paycheck1 = 0
paycheck2 = 0
print( "There are " + str(bankAmount) + " dollars in your bank account" )

 

######################

somelist = [3, 5, 3.2, 98, "bob", 45]
somelist.append(35)
print( somelist )

 

#####################

myspheres = []
for vari in range(10):
    #print(vari)
    baseSphere = mc.polySphere(sx=20.4, r=1, sy=20, ax=[0, 1, 0], cuv=2, ch=1 )
    myspheres.append( baseSphere[0] )
    print(baseSphere)
    mc.move( vari, 0, 0, r=True)
print( myspheres )

 

#####################################

import maya.cmds as mc
import random

cylHeight = int( raw_input() )

myListOfRotValues = range( 0, 360, 20 )
print( myListOfRotValues )

spokeObjectNames = []
for curCyl in myListOfRotValues:
    curSpoke = mc.polyCylinder( r=0.1, h=cylHeight )
    spokeObjectNames.append( curSpoke[0] )
    mc.move( 0, cylHeight/2.0 + 1, 0 )
    mc.move( 0, 0, 0, curSpoke[0]+".scalePivot", curSpoke[0]+".rotatePivot" )
    randRot = random.uniform( 0, 360 )
    mc.rotate( randRot, 0, 0 )
    
print( spokeObjectNames )
mc.group( spokeObjectNames )


#2

