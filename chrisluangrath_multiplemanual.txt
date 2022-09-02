import maya.cmds as mc

def make_planks(numbers):
    mc.polyCube (w=1, h=1, d=1, sx=1, sy=1, sz=1, ax=[1, 0, 0], cuv=4, ch=1)
    mc.scale( 7.255556, 0.438844, 1.866667 )

    for _ in range(numbers):
        mc.duplicate(rr = True)
        mc.move(4, z=True, relative = True)

def make_track(number):
    size = 3.88 * (number + 1)
    mc.polyCube (w=1, h=1, d=1, sx=1, sy=1, sz=1, ax=[1,0,0], cuv=4, ch=1)
    mc.move(-2,0,size/2)
    mc.scale(1, 0.29078, size )
    mc.move(0.219422, y=True )
    mc.duplicate(rr=True)
    mc.move( 4, x=True ,relative = True)

itr = 10
make_planks(5)
make_track(5)