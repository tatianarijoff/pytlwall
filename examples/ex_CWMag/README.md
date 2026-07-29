# Coated wall with magnetic boundary (`ex_CWMag`)

Same structure as [`ex_CW`](../ex_CW/README.md), but the outer boundary is a
**dispersive magnetic material**. Use this case to see how a magnetic boundary
changes the impedance with respect to a purely resistive one.

## Chamber

Radius **24.25 mm**, length 1 m, `betax = betay = 1`.

| Layer | Thickness | Conductivity | Magnetic properties |
|-------|-----------|--------------|---------------------|
| `layer0` | 1 mm | 1.670007·10⁶ S/m | non-magnetic |
| `boundary` (`CW`) | semi-infinite | 10⁶ S/m | µ_inf = 500, f_relax = 10 kHz |

The boundary permeability follows a single-pole relaxation model: `muinf_Hz`
is the initial relative permeability, `k_Hz` the relaxation frequency.

## Beam

`gammarel = 10000`, transverse test offset 10 mm.

## Frequency grid

Decimal exponents 2 to 11, i.e. 100 Hz to 10¹¹ Hz.

## Running

```bash
python examples/ex_CWMag.py
```

No `[output]` section, so `python -m pytlwall -a` does not apply.
