# Low-beta beam (`ex_lowbeta`)

A slow, non-ultrarelativistic beam. At `gammarel = 2.49` the space-charge
contributions are large, which makes this the reference case for the direct
and indirect space-charge impedances (`ZLongDSC`, `ZLongISC`, `ZTransDSC`,
`ZTransISC`).

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
python examples/ex_lowbeta.py
```

No `[output]` section here. The same chamber **with** output sections, ready
for batch execution, is in [`ex_run_exec`](../ex_run_exec/README.md).
