import gdsfactory as gf
from cspdk.si220 import cells

nm = 1e-3


@gf.cell
def sample_all_angle() -> gf.Component:
    """Example of a component with all angles."""
    c = gf.Component()
    w = cells.straight(length=4 * nm, width=4 * nm)
    w1 = c.create_vinst(w)
    w1.rotate(30)

    w2 = c.create_vinst(w)
    w2.connect("o1", w1["o2"])
    return c
