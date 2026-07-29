# Coated wall (`ex_CW`)

Circular chamber with a thin resistive coating, closed by a highly conductive
wall rather than by a perfect conductor. The reference case for a coated-wall
geometry.

## Chamber

Radius **18.4 mm**, length 1 m, `betax = betay = 1`.

| Layer | Thickness | Conductivity |
|-------|-----------|--------------|
| `layer0` | 0.5 µm | 10⁶ S/m |
| `boundary` (`CW`) | semi-infinite | 10⁹ S/m |

Both layers are non-magnetic and non-dispersive.

## Beam

`gammarel = 10000`, transverse test offset 10 mm.

## Frequency grid

Decimal exponents 0 to 12, i.e. 1 Hz to 10¹² Hz.

## Running

```bash
python examples/ex_CW.py
```

The configuration has no `[output]` section, so it cannot be run with
`python -m pytlwall -a`. Use the driver script, or load it from Python:

```python
from pytlwall import CfgIo
wall = CfgIo("examples/ex_CW/ex_CW.cfg").read_pytlwall()
ZLong = wall.ZLong
```
