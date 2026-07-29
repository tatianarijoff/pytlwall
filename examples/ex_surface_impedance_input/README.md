# Surface impedance from file (`ex_surface_impedance_input`)

The inverse of [`ex_surface_impedance`](../ex_surface_impedance/README.md):
instead of computing the surface impedance from the layer properties, it is
**read from a text file** and applied to the layer. Use this when the wall
response comes from a measurement or from an external code.

## Files

| File | Content |
|------|---------|
| `ex_surface_impedance_input.cfg` | chamber, beam and frequency definition |
| `surface_impedance_input.txt` | tabulated surface impedance |

The text file has a two-line header followed by three columns: frequency in
Hz, then the real and imaginary parts of the surface impedance.

## Chamber

Radius **35 mm**, length 1 m, `betax = betay = 1`.

| Layer | Thickness | Conductivity |
|-------|-----------|--------------|
| `layer0` | 1.5 mm | 833333 S/m |
| `boundary` (`V`) | semi-infinite vacuum | — |

The layer properties are overridden by the tabulated surface impedance.

## Beam

`gammarel = 2.49`, transverse test offset 10 mm.

## Running

```bash
python examples/ex_surface_impedance_input.py
```
