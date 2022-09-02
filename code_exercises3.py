import maya.cmds as mc
'''
3. Write a program in the Maya script editor that makes a brick wall.
'''

brick_height = 1.5
# small_brick_width = 2
# brick_width = 4
brick_width = 3.0
small_brick_width = brick_width/2
buffer = .2

blocks = []
def make_brick():
    block = mc.polyCube (w=brick_height, h=brick_width, d=1, sx=1, sy=1, sz=1, ax=[1, 0, 0], cuv=4, ch=1)
    blocks.append(block)

def make_brick_half():
    block = mc.polyCube (w=brick_height, h=small_brick_width, d=1, sx=1, sy=1, sz=1, ax=[1, 0, 0], cuv=4, ch=1)
    blocks.append(block)
    
def make_row(height, width):
    row_pos = 1.5
    for _ in range(width):
        make_brick()
        mc.move(row_pos, height, 0)
        row_pos += brick_width + buffer

def make_row_alt(height, width):
    small_buffer = .5
    # this is .25 if small_brick_width is 2
    row_pos = small_brick_width/2
    make_brick_half()
    mc.move(row_pos, height, 0)
    # row_pos += small_brick_width * 1.25 + buffer
    row_pos += small_brick_width * (1+small_buffer) + buffer

    for _ in range(width-1):
        make_brick()
        mc.move(row_pos, height, 0)
        row_pos += brick_width + buffer

    row_pos -= small_brick_width * small_buffer
    make_brick_half()
    mc.move(row_pos, height, 0)

def make_wall(height, width):
    blocks = []
    height_pos = 0
    for x in range(height):
        if x % 2 == 1:
            make_row(height_pos,width)
        else:
            make_row_alt(height_pos, width)
        height_pos += brick_height + buffer

    fill_width = (brick_width + buffer) * width
    block = mc.polyCube (w=height_pos-buffer, h=fill_width, d=.75, sx=1, sy=1, sz=1, ax=[1, 0, 0], cuv=4, ch=1)
    blocks.append(block)
    mc.move(fill_width/2, (height_pos - brick_height)/2 - buffer, 0)


make_wall(5,5)