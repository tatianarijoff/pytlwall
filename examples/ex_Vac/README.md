# Vacuum boundary (`ex_Vac`)

Single resistive layer backed by semi-infinite vacuum. Together with
[`ex_PEC`](../ex_PEC/README.md) this is the natural pair for studying the
effect of the outer boundary condition: same kind of wall, opposite closure.

## Chamber

Radius **18.4 mm**, length 1 m, `betax = betay = 1`.

| Layer | Thickness | Conductivity |
|-------|-----------|--------------|
| `layer0` | 1 mm | 1.67·10⁶ S/m |
| `boundary` (`V`) | semi-infinite vacuum | — |

## Beam

`gammarel = 10000`, transverse test offset 10 mm.

## Frequency grid

Decimal exponents 0 to 15, i.e. 1 Hz to 10¹⁵ Hz — the widest range of the
example set.

## Running

```bash
python examples/ex_Vac.py
```

No `[output]` section, so `python -m pytlwall -a` does not apply.
