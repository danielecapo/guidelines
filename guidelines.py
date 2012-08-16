import  fontforge

# FontForge Fit Curve v0.1

# Copyright (c) 2012, Daniele Capo (capo.daniele@gmail.com)

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# Redistributions of source code must retain the above copyright notice, this
# list of conditions and the following disclaimer.
#
# Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.
#
# The name of the author may not be used to endorse or promote products
# derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR IMPLIED
# WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO
# EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS;
# OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR
# OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
# ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


# A script for manipulating control points of a bezier curve to make it
# more 'square' or more 'round'.
# I've seen a similar feature in Glyphs (glyphsapp.com).
# To use it, select at least two consecutive points,
# then run the fit curve script under Tools menu,
# enter a number (0 retract the handles, the curve becomes a line,
# with 100 the two handles are extended until they touch,
# if you enter a number greater than 100, handles cross,
# the curve becomes concave).
# If the handles of the selected bezier segment are parallel,
# or the segment is a line, nothing happens

# Place this script in ~/.FontForge/python/ as usual

# get selected points in a contour
def selected_points (contour):
    return filter (lambda (p): p.selected, contour)
        
#direction can be 'h', 'v' or 'hv'

def add_guides (glyph, direction):
    f = fontforge.activeFont()
    guides = f.guide
    l = glyph.layers[glyph.activeLayer]
    for c in l:
        for p in selected_points(c):
            if direction == 'h' or direction == 'hv':
                guide = fontforge.contour()
                #place an horizontal guideline using point position
                guide.moveTo (-1000, p.y)
                guide.lineTo (2000, p.y)
                guides += guide
            if direction == 'v' or direction == 'hv':
                guide = fontforge.contour()
                #place a vertical guideline using point position
                guide.moveTo (p.x, -2000)
                guide.lineTo (p.x, 3000)
                guides += guide
            else:
                return False
           
            f.guide = guides
    glyph.layers[glyph.activeLayer]=l
    #Is there a better way to refresh the screen?
    print 'done'
    return True

if fontforge.hasUserInterface():
    menuText_h  = "Horizontal guidelines"
    menuText_v  = "Vertical guidelines"
    menuText_hv = "Hor/Vert guidelines"


    fontforge.registerMenuItem(lambda r, g: add_guides (g, 'h') ,\
                                   None, None, \
                                   "Glyph", None, menuText_h)
    fontforge.registerMenuItem(lambda r, g: add_guides (g, 'v') ,\
                                   None, None, \
                                   "Glyph", None, menuText_v)
    fontforge.registerMenuItem(lambda r, g: add_guides (g, 'hv') ,\
                                   None, None, \
                                   "Glyph", None, menuText_hv)
