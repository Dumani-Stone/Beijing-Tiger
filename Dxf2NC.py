#!/usr/bin/env python3
# NOTES:
# - to run: `./Dxf2NC.py path/to/dxf_file.dxf`
# - The WCS origin for all parts is the bottom left corner
# - all coords are absolute

import sys
import ezdxf

# NC Params
ncwcs = 'G54' # X0 should be relative to inside face of left blade
ncunits = 'G20'
ncrapid = 'G00' # mv() appends XYZ coords to this


# coord = (X,Y,Z)
# rapid = bool, if true uses ncrapid
def mv(coord, feed, rapid):
    if rapid == true:
        return '{ncrapid} X{coord[0]} Y{coord[1]} Z{coord[2]} '
    else:
        return 'G01 X{coord[0]} Y{coord[1]} Z{coord[2]} F{feed}'

# files
dxf_file = sys.argv[1] # input
nc_file = sys.argv[2] # output

# movement bounds (abs to ncwcs)
z_top = 5 # top of stock
z_retract = 8 # retract height
y_ext = .25 # extend y travel equally on both sides

# zoff = offset to add to all Z values
def cut(stepdown, stepover, feed, plunge_feed, rpm, zoff):
    cur_stepover = 1 # if 0: saw would skim part
    cur_stepdown = 0
    dxf_height = 0 # dxf height @ cur_stepover
    # Overview:
    # loop: (for each stepover)
    #   Rapid(stepover*cur_stepover, -y_ext, z_retract)
    #   Find dxf height @ current X pos
    #   loop: (til saw is @ dxf height)
    #       if (z_top-stepdown*(cur_stepdown+1) < dxf_height):
    #           (z_top-(stepdown*cur_stepdown))-dxf_height
    #           break
    #       else:
    #           Plunge(Z=z_top-stepdown)
    pass
