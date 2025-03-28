import gdsfactory as gf
from cspdk.si220 import cells


@gf.cell
def dbr(w1=0.5, w2=0.55, cross_section="xs_sc") -> gf.Component:
    c = gf.c.dbr(w1=w1, w2=w2, cross_section=cross_section)
    return c
