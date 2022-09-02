'''
2. Write a program in the Maya script editor that takes in user 
input telling the program what type of object to create. If they 
type "sphere", then create a sphere. If they type "box", then 
create a box. If they type "cone", then create a cone. Otherwise, 
tell them they typed a wrong input.
'''
import maya.cmds as mc

def make_shape():
    text = None
    shapes = ['sphere','box','cone']
    while text == None:
        result = mc.promptDialog(
            title = 'Shape Make',
            message = 'Enter a shape to make (sphere, box, cone)',
            # button=['sphere','box','cone']
            defaultButton='Ok',
            cancelButton='Cancel',
            dismissString='Cancel'
        )   

        if result == 'Confirm':
            input = mc.promptDialog(query=True, text=True)
            if input.lower() in shapes:
                text = input.lower()
                print(text)
                if text == 'sphere':
                    mc.polySphere(sx=20.4, r=1, sy=20, ax=[0, 1, 0], cuv=2, ch=1 )
                elif text == 'box':
                    mc.polyCube (w=1, h=1, d=1, sx=1, sy=1, sz=1, ax=[1, 0, 0], cuv=4, ch=1)
                elif text == 'cone':
                    mc.polyCone(r=1, h=1    )


make_shape()