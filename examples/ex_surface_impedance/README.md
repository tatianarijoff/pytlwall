# Equivalent surface impedance (`ex_surface_impedance`)

Demonstrates the **equivalent surface impedance** of a wall: `ZLongSurf` and
`ZTransSurf`, the quantities that condense a multilayer stack into a single
surface property.

The chamber is identical to [`ex_lowbeta`](../ex_lowbeta/README.md); what the
example adds is the extraction and plotting of the surface quantities rather
than the coupling impedances.

## Chamber

Radius **35 mm**, length 1 m, `betax = betay = 1`.

| Layer | Thickness | Conductivity |
|-------|-----------|--------------|
| `layer0` | 1.5 mm | 833333 S/m |
| `boundary` (`V`) | semi-infinite vacuum | — |

## Beam

`gammarel = 2.49`, transverse test offset 10 mm.

## Frequency grid

Decimal exponents 0 to 10, i.e. 1 Hz to 10¹⁰ Hz.

## Running

```bash
python examples/ex_surface_impedance.py
```

The natural counterpart is
[`ex_surface_impedance_input`](../ex_surface_impedance_input/README.md), which
goes the other way: it reads a surface impedance from file instead of
computing it.
