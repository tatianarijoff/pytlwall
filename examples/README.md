# Examples

Configuration-driven examples. Each folder holds one or more `.cfg` files and
a `README.md` describing the chamber, the beam and how to run it.

For the **Python API** — using `Beam`, `Frequencies`, `Layer`, `Chamber`,
`TlWall` and `MultipleChamber` directly from code — see the module guides
under [`doc/`](../doc/EXAMPLES.md) instead. The two sets are complementary:
this directory covers the configuration-file workflow, `doc/EXAMPLES_*.md`
covers the programmatic one.

## Frequency-domain examples

| Folder | What it shows | Batch |
|--------|---------------|:-----:|
| [`ex_CW`](ex_CW/README.md) | Thin coating on a highly conductive wall | — |
| [`ex_CWMag`](ex_CWMag/README.md) | Dispersive magnetic boundary | — |
| [`ex_PEC`](ex_PEC/README.md) | Two layers on a perfect conductor; hand-written and machine-written configurations | — |
| [`ex_Vac`](ex_Vac/README.md) | Same wall closed by semi-infinite vacuum | — |
| [`ex_lowbeta`](ex_lowbeta/README.md) | Slow beam, dominant space charge | — |
| [`ex_run_exec`](ex_run_exec/README.md) | **Full batch pipeline from the command line** | ✅ |
| [`ex_surface_impedance`](ex_surface_impedance/README.md) | Equivalent surface impedance of a wall | — |
| [`ex_surface_impedance_input`](ex_surface_impedance_input/README.md) | Surface impedance read from a text file | — |
| [`ex_multiple`](ex_multiple/README.md) | Impedance accumulated over a lattice of elements | — |
| [`ex_ferrite_kicker`](ex_ferrite_kicker/README.md) | **Four-layer kicker: coating, ceramic, vacuum gap, ferrite** | ✅ |

## Time-domain examples

| Folder | What it shows | Batch |
|--------|---------------|:-----:|
| [`ex_wake_pec`](ex_wake_pec/README.md) | Wake functions, perfect conductor boundary | — |
| [`ex_wake_vacuum`](ex_wake_vacuum/README.md) | Wake functions, vacuum boundary | — |

## Reading the "Batch" column

Only the two marked folders can be executed directly from the command line:

```bash
python -m pytlwall -a examples/ex_run_exec/ex_lowbeta.cfg
```

Batch mode runs the whole pipeline — build the chamber, compute the
impedances, write the data files, produce the plots — and it needs the
configuration to declare what to produce, through `[output]`, `[outputN]` and
`[img_outputN]` sections.

The other configurations define a valid **model** but no output, so a batch
run exits with a warning and writes nothing. They are meant to be loaded from
their driver script in `examples/`, or from your own code:

```python
from pytlwall import CfgIo

wall = CfgIo("examples/ex_CW/ex_CW.cfg").read_pytlwall()
ZLong = wall.ZLong
```

Adding the missing sections to any of them is enough to make it runnable;
[`ex_run_exec`](ex_run_exec/README.md) is the template to copy from.

## Suggested reading order

1. [`ex_run_exec`](ex_run_exec/README.md) — see the whole pipeline work
2. [`ex_PEC`](ex_PEC/README.md) and [`ex_Vac`](ex_Vac/README.md) — the effect
   of the outer boundary
3. [`ex_CWMag`](ex_CWMag/README.md) — dispersive magnetic materials
4. [`ex_ferrite_kicker`](ex_ferrite_kicker/README.md) — everything combined in
   a realistic four-layer element

## Conventions

- `fmin` and `fmax` are **decimal exponents**, not frequencies: `fmin = 3`
  means 10³ Hz. `fstep` sets the point density, and larger values give more
  points.
- Relative output paths resolve against the **working directory**, unless the
  configuration declares `main_path` in a `[path_info]` section. Run the
  examples from the repository root.
- Generated results under `examples/*/output/`, `examples/*/img/` and
  `examples/*/sav/` are excluded from version control.
- `sigmaDC = 0` is not admitted; use a negligible value such as `1e-12` for an
  insulator.
