# Perfect conductor boundary (`ex_PEC`)

Two-layer chamber closed by a perfect electric conductor. This folder holds
**two configurations describing the same physics**.

| File | Origin |
|------|--------|
| `ex_PEC.cfg` | hand-written, with comments |
| `ex_PEC2.cfg` | written back out by `CfgIo`, uncommented |

`ex_PEC2.cfg` is useful as a round-trip reference: it shows the exact layout
the package produces when saving a configuration, including empty keys in the
`[boundary]` section and an empty `freq_file` entry. Both files give identical
results.

## Chamber

Radius **18.4 mm**, length 1 m, `betax = betay = 1`.

| Layer | Thickness | Conductivity |
|-------|-----------|--------------|
| `layer0` | 50 µm | 1.82·10⁹ S/m |
| `layer1` | 1 mm | 1.67·10⁶ S/m |
| `boundary` | PEC | — |

## Beam

`gammarel = 10000`, transverse test offset 10 mm.

## Frequency grid

Decimal exponents 0 to 13, i.e. 1 Hz to 10¹³ Hz.

## Running

```bash
python examples/ex_PEC.py
```

No `[output]` section in either file, so `python -m pytlwall -a` does not apply.
