# Ferrite kicker example

A four-layer circular chamber representing a ferrite kicker: a titanium-coated
ceramic tube, a vacuum gap, and a ferrite yoke closed by a perfect conductor.

This is the most complex configuration shipped with the package. It exercises
several features at once — multiple layers, a dispersive magnetic material, a
vacuum layer between two solid ones, and a PEC boundary — which makes it a
useful reference case when comparing implementations.

## Chamber

Beam pipe radius: **10 mm**. Length 1 m, `betax = betay = 1`, so the result is
an impedance per metre at unit beta function.

| Layer | Material | Thickness | Key properties |
|-------|----------|-----------|----------------|
| `layer0` | Titanium coating | 1 µm | σ = 2·10⁶ S/m |
| `layer1` | Ceramic tube | 5 mm | ε_r = 9, σ = 10⁻¹² S/m |
| `layer2` | Vacuum gap | 2 mm | — |
| `layer3` | Ferrite yoke | 15 mm | µ_inf = 460, f_relax = 20 MHz, ε_r = 12, σ = 10⁻⁴ S/m |
| `boundary` | PEC | — | perfect electric conductor |

Layers are ordered from the beam outwards. Any property not stated explicitly
in the configuration keeps the pytlwall default for a non-magnetic,
non-dispersive material.

Two conventions are worth noting:

- The ceramic conductivity is set to `1e-12` rather than zero, because
  `sigmaDC = 0` is not admitted by the layer model.
- The ferrite permeability follows a single-pole relaxation model: `muinf_Hz`
  is the initial relative permeability and `k_Hz` the relaxation frequency.

## Beam

Ultrarelativistic protons, `gammarel = 7000`, transverse test offset 1 mm.

## Frequency grid

`fmin` and `fmax` are decimal exponents, so the grid spans 10² Hz to 10¹⁰ Hz.
`fstep = 3` sets the point density — larger values give more points. This
configuration produces **7200 frequencies** from 101 Hz to 10 GHz, which is why
the run takes noticeably longer than the other examples.

## Running

From the repository root:

```bash
python -m pytlwall -a examples/ex_ferrite_kicker/01_ferrite_kicker.cfg
```

Output paths in the configuration are relative to the working directory, so
running from elsewhere will place the results elsewhere. To run from an
arbitrary directory, add a `[path_info]` section with `main_path` set to the
repository root.

## Output

```
examples/ex_ferrite_kicker/
├── output/
│   └── ferrite_kicker.xlsx     all twelve impedances, real and imaginary
└── img/
    ├── ZLong.png               longitudinal impedance
    └── ZDip.png                horizontal and vertical dipolar impedance
```

Both directories are created automatically on the first run and are excluded
from version control by the repository `.gitignore`, along with the other
`examples/*/output/` and `examples/*/img/` paths.

## Expected magnitudes

Longitudinal impedance, for a quick sanity check after a change:

| f [Hz] | Re(ZLong) [Ω] | Im(ZLong) [Ω] |
|--------|---------------|---------------|
| 10³ | 5.83·10⁻² | 1.34·10⁻¹ |
| 10⁵ | 7.89 | 7.23·10⁻¹ |
| 10⁶ | 7.95 | 7.33·10⁻² |
| 10⁷ | 7.95 | 7.62·10⁻³ |
| 10⁸ | 7.95 | 3.36·10⁻³ |
| 10⁹ | 7.96 | 4.09·10⁻² |

The real part rises through the low-frequency range and then flattens above
roughly 10⁵ Hz, while the imaginary part falls away over the same interval.

These values are recorded as a regression baseline for this implementation,
not as an independently validated physical result.
