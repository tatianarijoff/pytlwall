# Batch execution (`ex_run_exec`)

The reference example for the **command-line batch mode**. Physically it is
the same chamber as [`ex_lowbeta`](../ex_lowbeta/README.md); what differs is
that this configuration declares `[output]`, `[output1]`, `[output2]` and
`[img_output1]` sections, so the full pipeline runs end to end without writing
any Python.

Use it as the template when writing your own runnable configuration.

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

From the repository root:

```bash
python -m pytlwall -a examples/ex_run_exec/ex_lowbeta.cfg
```

## Output

Written into this folder:

| File | Content |
|------|---------|
| `low_beta.xlsx` | all twelve impedances, real and imaginary |
| `low_beta_long.txt` | `ZLong`, `ZLongSurf`, `ZLongDSC`, `ZLongISC` |
| `low_beta_long.png` | longitudinal impedance plot |

All three are excluded from version control.

Output paths in the configuration are relative to the working directory, so
run this from the repository root or the files will land elsewhere.
