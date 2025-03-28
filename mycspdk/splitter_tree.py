import gdsfactory as gf
from cspdk.si220 import cells


@gf.cell
def splitter_tree(cross_section="xs_sc", **kwargs) -> gf.Component:
    c = gf.c.splitter_tree(cross_section=cross_section, **kwargs)
    return c
