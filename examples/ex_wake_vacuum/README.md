# Time-domain wake, vacuum boundary (`ex_wake_vacuum`)

Identical to [`ex_wake_pec`](../ex_wake_pec/README.md) except for the outer
boundary, which here is semi-infinite vacuum instead of a perfect conductor.
The two cases exist to be compared: same wall, opposite closure.

## Chamber

Radius **22 mm**, length 1 m, `betax = betay = 1`.

| Layer | Thickness | Conductivity |
|-------|-----------|--------------|
| `layer0` | 2 mm | 5.96·10⁷ S/m (copper) |
| `boundary` (`V`) | semi-infinite vacuum | — |

## Beam

`gammarel = 7460.52`, transverse test offset 10 mm.

## Time grid

Decimal exponents −12 to −1, i.e. 1 ps to 100 ms, over **1401 logarithmically
spaced points**.

## Running

```bash
python examples/ex_wake.py
```

The driver computes both boundary conditions and plots them together.

## Further reading

- [WAKE.md](../../doc/WAKE.md) — module overview and usage
- [WAKE_THEORY.md](../../doc/WAKE_THEORY.md) — transmission-line wake, thick
  and thin wall limits
