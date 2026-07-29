# Multi-chamber lattice (`ex_multiple`)

Accumulates the impedance of a whole sequence of elements through
`pytlwall.MultipleChamber`, rather than treating a single chamber. Each element
of the lattice is assigned a chamber type, and its own geometry and optics.

## Files

| File | Role |
|------|------|
| `apertype2.txt` | chamber type of each element, one per line |
| `b_L_betax_betay.txt` | radius, length and beta functions per element |
| `Round.cfg`, `Oblong.cfg`, `Rectangular.cfg`, `Diamond.cfg` | material definition per chamber type |

`apertype2.txt` lists **10 elements** using three types: `round`, `oblong`
and `rectangular`. `b_L_betax_betay.txt` carries the matching 10 rows of
geometry and optics, after a two-line comment header.

## Chamber types

| Type | Shape | Layers |
|------|-------|--------|
| `Round`, `Oblong` | circular, radius 18.4 mm | 50 µm at 1.82·10⁹ S/m, then a second layer |
| `Rectangular`, `Diamond` | rectangular, 31.5 × 11.5 mm | single layer, 0.4 mm |

Note that `betarel` is used here instead of `gammarel`: 1.0 for the circular
types and 0.916 for the rectangular ones. The transverse test offset is 3 mm.

## Known redundancy

`Diamond.cfg` is byte-identical to `Rectangular.cfg`, and `Oblong.cfg` to
`Round.cfg`. Since `apertype2.txt` never requests a `diamond` element,
`Diamond.cfg` is unused by this example. The duplicates are kept because the
file names are what `MultipleChamber` looks up by chamber type; they are
placeholders awaiting distinct definitions, not four independent cases.

## Running

```bash
python examples/example_multiple_chamber.py
```
