import maya.cmds as mc

plank_length = 2
plank_spacing = 4
plank_height = 0.438844
nut_spacing = 3.2

def make_planks(numbers):
    
    width = 7.255556
    bolt_spacing_radius = 6
    # length = 2

    plank = mc.polyCube (w=plank_height, h=width, d=plank_length, sx=1, sy=1, sz=1, ax=[1, 0, 0], cuv=4, ch=1)
    nut1 = mc.polyCylinder(r=.25, h=0.1, sx=8, sy=2, sz =1, ax=[0,1,0], rcp=0, cuv=3, ch=1)
    mc.move((plank_height + nut_height)/2, y=True)
    mc.move(nut_spacing, x=True)
    nut2 = mc.duplicate(rr = True)
    mc.move(nut_spacing*-1, x=True)
    mc.select(plank, nut1, nut2)
    for _ in range(numbers):
        mc.duplicate(n=plank[0],rr = True)
        mc.move(plank_spacing, z=True, relative = True)

def make_track(number):
    height = .3 # .6
    width = 1
    length = plank_length * (number) + plank_spacing * (number - 1)
    track_radius = 2.3
    # hole1 = mc.polyCube (w=height/3, h=width, d=length, sx=1, sy=1, sz=1, ax=[1,0,0], cuv=4, ch=1)
    # mc.move()
    mc.polyCube (w=height, h=width, d=length, sx=1, sy=1, sz=1, ax=[1,0,0], cuv=4, ch=1)

    mc.move(-track_radius,(height + plank_height)/2,length/2 - 1)
    mc.duplicate(rr=True)
    mc.move( track_radius*2, x=True ,relative = True)

itr = 10

def make_tracks(x):
    make_planks(x)
    make_track(x)

make_tracks(3)
nut_height = .1
