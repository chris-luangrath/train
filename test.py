import maya.cmds as mc

class PlankMaker():
#     # def __init__(self):
#     #     self.plank_counter = 1
#     #     self.plank = "plank"
    plank_counter = 1
    plank = "plank"
    def make_plank(self):
        plank1 = f"plank{self.plank_counter}"
    #     self.plank_counter += 1
    #     plank2 = f"plank{self.plank_counter}"
    #     mc.duplicate( plank1, n=plank2 )
    #     mc.select( plank2 )
    #     mc.move(4, z=True, relative = True)

    # def make_planks_loop(self):
    #     mc.polyCube ( n= (self.plank + str(self.plank_counter)), w=1, h=1, d=1, sx=1, sy=1, sz=1, ax=[1, 0, 0], cuv=4, ch=1)
    #     mc.scale( 7.255556, 0.438844, 1.866667 )
    #     for _ in range(10):
    #         self.make_plank

    # def make_planks_many(self):
    #     mc.polyCube ( n= (self.plank + str(self.plank_counter)), w=1, h=1, d=1, sx=1, sy=1, sz=1, ax=[1, 0, 0], cuv=4, ch=1)
    #     mc.scale( 7.255556, 0.438844, 1.866667 )


    #     mc.duplicate( 'plank1', n='plank2' )
    #     mc.select( 'plank2' )
    #     mc.move(4, z=True, relative = True)
    #     # mc.move( r=pr, z=4 )

    #     mc.duplicate( 'plank2', n="plank3")
    #     mc.select( 'plank3' )
    #     mc.move(4, z=True, relative = True)
    #     mc.duplicate('plank3', n="plank4")
    #     mc.select( 'plank4' )
    #     mc.move( 12, z=True )
    #     mc.duplicate( 'plank4', n='plank5')
    #     mc.select( "plank5" )
    #     mc.move( 0,0,16 ) # testing other way, nice nice nice
    #     mc.polyCube ( n='track1', w=1, h=1, d=1, sx=1, sy=1, sz=1, ax=[1,0,0], cuv=4, ch=1)
    #     mc.select("track1")
    #     mc.move(-2,0,8)
    #     mc.scale(1, 0.29078, 21.311112 )
    #     mc.move(0.219422, y=True )
    #     mc.duplicate( 'track1', n="track2")
    #     mc.select('track2')
    #     mc.move( 2, x=True )

# pm = PlankMaker()
print("heyo")
# pm.make_planks_loop()
