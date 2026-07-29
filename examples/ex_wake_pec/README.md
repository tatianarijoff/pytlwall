# Time-domain wake, PEC boundary (`ex_wake_pec`)

A **time-domain** case: it computes wake functions rather than impedances,
through the `TLWallWake` class. Selected by `CalcWake = wake` in the
`[calc_info]` section, which replaces `[frequency_info]` with `[time_info]`.

## Chamber

Radius **22 mm**, length 1 m, `betax = betay = 1`.

| Layer | Thickness | Conductivity |
|-------|-----------|--------------|
| `layer0` | 2 mm | 5.96·10⁷ S/m (copper) |
| `boundary` | PEC | — |

## Beam

`gammarel = 7460.52`, transverse test offset 10 mm.

## Time grid

Decimal exponents −12 to −1, i.e. 1 ps to 100 ms, over **1401 logarithmically
spaced points**.

## Running

```bash
python examples/ex_wake.py
```

The driver runs this case together with
[`ex_wake_vacuum`](../ex_wake_vacuum/README.md) and compares the two boundary
conditions on the same wall.

## Further reading

- [WAKE.md](../../doc/WAKE.md) — module overview and usage
- [WAKE_THEORY.md](../../doc/WAKE_THEORY.md) — transmission-line wake, thick
  and thin wall limits
