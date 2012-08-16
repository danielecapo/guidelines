import  fontforge

def selected_points (contour):
    return filter (lambda (p): p.selected, contour)
        
def add_guides (glyph, direction):
    f = fontforge.activeFont()
    guides = f.guide
    l = glyph.layers[glyph.activeLayer]
    for c in l:
        for p in selected_points(c):
            guide = fontforge.contour()
            if direction == 'h' or direction == 'hv':
                guide.moveTo (-1000, p.y)
                guide.lineTo (2000, p.y)
            elif direction == 'v' or direction == 'hv':
                guide.moveTo (p.x, -2000)
                guide.lineTo (p.x, 3000)
            else:
                return False
            guides += guide
            f.guide = guides
    glyph.layers[glyph.activeLayer]=l
    print 'done'
    return True

if fontforge.hasUserInterface():
    keyShortcut = None
    menuText_h = "Horizontal guidelines"
    menuText_v = "Vertical guidelines"

    fontforge.registerMenuItem(lambda r, g: add_guides (g, 'h') ,\
                                   None, None, \
                                   "Glyph", keyShortcut, menuText_h)
    fontforge.registerMenuItem(lambda r, g: add_guides (g, 'v') ,\
                                   None, None, \
                                   "Glyph", keyShortcut, menuText_v)
