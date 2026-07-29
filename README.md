# PyTlWall

![PyTlWall Logo](logo005.png)

**Python Transmission Line Wall Impedance Calculator**

---

## Overview

PyTlWall is a Python implementation of the **Transmission Line Impedance Model** for computing beam coupling impedances in particle accelerator vacuum chambers.

### Key Features

| Feature | Description |
|---------|-------------|
| **TL Model** | Longitudinal & transverse impedance calculation |
| **Multilayer** | Arbitrary number of material layers |
| **Chamber Types** | Circular, elliptical, rectangular cross-sections |
| **Yokoya Factors** | Automatic geometric correction factors |
| **Space Charge** | Direct and indirect space charge impedances |
| **Batch Mode** | Multi-chamber lattice processing |
| **GUI** | Qt-based configuration editor and visualizer |
| **Plotting** | Automatic impedance plots |
| **Export** | Excel/CSV data export |

---

## Authors

- **Tatiana Rijoff** - tatiana.rijoff@gmail.com
- **Carlo Zannini** - carlo.zannini@cern.ch

*Copyright: CERN*

### Reference

**Electromagnetic Simulation of CERN Accelerator Components and Experimental Applications**  
Author: **Carlo Zannini**

---

## Installation

### Requirements

| Component | Version | Notes |
|-----------|---------|-------|
| Python | ≥ 3.9 | Required |
| NumPy | latest | Required |
| SciPy | latest | Required |
| Matplotlib | latest | Required for plotting |
| openpyxl | latest | Required for Excel export |
| PyQt5 | latest | Optional, for GUI |

### Standard Installation

> **Repository and package name**
> Repository, working directory and importable package all share the same
> name, `pytlwall`. The repository was previously called `TLWallNew`; old
> links still redirect, but the current name is `pytlwall`.
> Do not confuse it with `pytlwall-v1`, which holds the superseded v1
> codebase and is kept for reference only.

```bash
# Clone the repository
git clone https://github.com/tatianarijoff/pytlwall.git
cd pytlwall

# Install package
pip install .
```

### Sources

| Source | URL | Status |
|--------|-----|--------|
| **pytlwall** (current) | https://github.com/tatianarijoff/pytlwall | Active development |
| pytlwall-v1 (legacy) | https://github.com/tatianarijoff/pytlwall-v1 | Superseded, reference only |

### Development Installation

```bash
# Install in editable mode
pip install -e .

# Install with all dependencies
pip install -e ".[dev,gui]"
```

### Virtual Environment (recommended)

On Debian, Ubuntu and other distributions that ship an externally managed
Python, `pip install` against the system interpreter is refused with
`error: externally-managed-environment` (PEP 668). Install into a virtual
environment instead:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```

The shell prompt is prefixed with `(.venv)` while the environment is active.
Reactivate it in every new terminal with `source .venv/bin/activate`, and
leave it with `deactivate`.

If `python3 -m venv` fails, install the system package first:
`sudo apt install python3-venv`.

Note that Debian and Ubuntu provide `python3` only: a bare `python` command
does not exist outside an activated virtual environment.

On Windows the activation command is `.venv\Scripts\activate`.

### Conda Environment

```bash
conda create -n pytlwall python=3.12
conda activate pytlwall
pip install .
```

### GUI Dependencies

```bash
# For graphical interface
pip install pyqt5
```

---

## Quick Start

### Minimal Example

```python
from pytlwall import Beam, Frequencies, Layer, Chamber, TlWall

# 1. Define beam parameters (LHC 7 TeV protons)
beam = Beam(gammarel=7460.52)

# 2. Define frequency range (1 kHz to 1 GHz)
freqs = Frequencies(fmin=3, fmax=9, fstep=2)

# 3. Define chamber geometry
chamber = Chamber(
    pipe_rad_m=0.022,
    chamber_shape='CIRCULAR'
)

# 4. Define material layer
copper = Layer(
    thick_m=0.001,
    sigmaDC=5.96e7,
    freq_Hz=freqs.freq
)
chamber.layers = [copper]

# 5. Calculate impedances
wall = TlWall(chamber=chamber, beam=beam, frequencies=freqs)
ZLong = wall.calc_ZLong()
ZTrans = wall.calc_ZTrans()

print(f"Calculated at {len(freqs)} frequencies")
print(f"Max |ZLong|: {abs(ZLong).max():.3e} Ω")
print(f"Max |ZTrans|: {abs(ZTrans).max():.3e} Ω/m")
```

### Using Configuration Files

```python
from pytlwall import CfgIo

# Load configuration and create TlWall
cfg = CfgIo("chamber.cfg")
wall = cfg.read_pytlwall()

# Calculate impedances
ZLong = wall.calc_ZLong()
ZTrans = wall.calc_ZTrans()
```

### Multi-Chamber Lattice

```python
from pytlwall import MultipleChamber

mc = MultipleChamber(
    apertype_file="apertype2.txt",
    geom_file="b_L_betax_betay.txt",
    input_dir="./input/",
    out_dir="./output/"
)

# Load inputs
mc.load()

# Calculate all elements
mc.calculate_all()

# Plot total accumulated impedances
mc.plot_totals(show=False)
```

---

## Running PyTlWall

### Command Line Interface

```bash
# Batch mode: run a full calculation from a configuration file
python -m pytlwall -a config.cfg

# Equivalent short form (a bare .cfg is treated as batch mode)
python -m pytlwall config.cfg

# Interactive text interface
python -m pytlwall -i

# Launch GUI
python -m pytlwall --gui

# Version
python -m pytlwall --version
```

After `pip install .` the same commands are available through the
`pytlwall` console script, e.g. `pytlwall -a config.cfg`.

> **Batch mode requires output sections.**
> `-a` executes the full pipeline: build the chamber/beam/frequency objects,
> compute the impedances, write the data files, produce the plots. The
> impedances to compute are taken from the `[output]` section, the data files
> from `[output1]`, `[output2]`, … and the images from `[img_output1]`,
> `[img_output2]`, …
> A configuration file containing only `[base_info]`, `[layers_info]`,
> `[boundary]`, `[frequency_info]` and `[beam_info]` is a valid *model*
> definition but produces no output in batch mode; the run exits with a
> warning. Most files under `examples/` are of this kind and are meant to be
> loaded from Python or from the GUI.
> `examples/ex_run_exec/ex_lowbeta.cfg` is the reference example of a
> complete, directly runnable configuration.

Relative output paths in the configuration are interpreted with respect to
the current working directory, unless a `[path_info]` section defines
`main_path`, in which case they are resolved against it.

### Launch GUI Directly

```bash
# Using the GUI module
python -m pytlwall_gui

# Or with the run script
python run_gui.py

# Or via main module
python -m pytlwall --gui
```

### Python Script

```python
import pytlwall

# Access all modules
beam = pytlwall.Beam(gammarel=7460.52)
freqs = pytlwall.Frequencies(fmin=3, fmax=9, fstep=2)
# ... etc
```

---

## Project Structure

### Core Modules

| Module | Description |
|--------|-------------|
| `beam.py` | Particle beam parameters with relativistic calculations |
| `frequencies.py` | Frequency array management |
| `layer.py` | Material layer definitions |
| `chamber.py` | Chamber geometry and Yokoya factors |
| `tlwall.py` | Main impedance calculation engine |
| `cfg_io.py` | Configuration file I/O |

### Utility Modules

| Module | Description |
|--------|-------------|
| `io_util.py` | Input/output helper functions |
| `plot_util.py` | Plotting utilities |
| `logging_util.py` | Logging system |
| `multiple_chamber.py` | Multi-element lattice processing |

### GUI Module

| Module | Description |
|--------|-------------|
| `pytlwall_gui/` | Qt-based graphical interface |

---

## Documentation

### API Reference

| Document | Description |
|----------|-------------|
| [API_REFERENCE.md](doc/API_REFERENCE.md) | Main API overview |
| [API_REFERENCE_BEAM.md](doc/API_REFERENCE_BEAM.md) | Beam module |
| [API_REFERENCE_FREQUENCIES.md](doc/API_REFERENCE_FREQUENCIES.md) | Frequencies module |
| [API_REFERENCE_LAYER.md](doc/API_REFERENCE_LAYER.md) | Layer module |
| [API_REFERENCE_CHAMBER.md](doc/API_REFERENCE_CHAMBER.md) | Chamber module |
| [API_REFERENCE_TLWALL.md](doc/API_REFERENCE_TLWALL.md) | TlWall module |
| [API_REFERENCE_CFGIO.md](doc/API_REFERENCE_CFGIO.md) | CfgIo module |
| [API_REFERENCE_MULTIPLE.md](doc/API_REFERENCE_MULTIPLE.md) | MultipleChamber module |

### GUI Documentation

| Document | Description |
|----------|-------------|
| [GUI.md](doc/GUI.md) | GUI overview and getting started |
| [GUI_MENU_BAR.md](doc/GUI_MENU_BAR.md) | Menu bar reference |
| [GUI_SIDEBAR.md](doc/GUI_SIDEBAR.md) | Sidebar controls |
| [GUI_DATA_PANEL.md](doc/GUI_DATA_PANEL.md) | Data panel usage |
| [GUI_PLOT_PANEL.md](doc/GUI_PLOT_PANEL.md) | Plot panel features |
| [GUI_VIEW_IO.md](doc/GUI_VIEW_IO.md) | View and I/O operations |

### Examples

| Document | Description |
|----------|-------------|
| [examples/README.md](examples/README.md) | Configuration-file examples: index |
| [EXAMPLES.md](doc/EXAMPLES.md) | Python API examples: overview |
| [EXAMPLES_BEAM.md](doc/EXAMPLES_BEAM.md) | Beam examples |
| [EXAMPLES_FREQUENCIES.md](doc/EXAMPLES_FREQUENCIES.md) | Frequencies examples |
| [EXAMPLES_LAYER.md](doc/EXAMPLES_LAYER.md) | Layer examples |
| [EXAMPLES_CHAMBER.md](doc/EXAMPLES_CHAMBER.md) | Chamber examples |
| [EXAMPLES_TLWALL.md](doc/EXAMPLES_TLWALL.md) | TlWall examples |
| [EXAMPLES_MULTIPLE.md](doc/EXAMPLES_MULTIPLE.md) | MultipleChamber examples |
| [EXAMPLES_LOGGING.md](doc/EXAMPLES_LOGGING.md) | Logging examples |
| [EXAMPLES_WAKE.md](doc/EXAMPLES_WAKE.md) | Wake examples |

### Time-Domain Wake

| Document | Description |
|----------|-------------|
| [WAKE.md](doc/WAKE.md) | Time-domain wake module (`TLWallWake`) overview and usage |
| [WAKE_THEORY.md](doc/WAKE_THEORY.md) | Physical model: transmission-line wake and thick/thin limits |
| [test_tlwall_wake.md](tests/doc/test_tlwall_wake.md) | Wake module test suite |

### Additional Documentation

| Document | Description |
|----------|-------------|
| [INSTALLATION.md](doc/INSTALLATION.md) | Detailed installation guide |
| [CHAMBER_SHAPES_REFERENCE.md](doc/CHAMBER_SHAPES_REFERENCE.md) | Chamber shape details |
| [PYTLWALL_THEORY.md](doc/PYTLWALL_THEORY.md) | Theoretical background |

---

## Configuration File Format

Example `.cfg` file:

```ini
[base_info]
component_name = arc_chamber
pipe_radius_m = 0.022
pipe_len_m = 1.0
chamber_shape = CIRCULAR
betax = 100.0
betay = 100.0

[layers_info]
nbr_layers = 1

[layer0]
type = CW
thick_m = 0.001
sigmaDC = 5.96e7
muinf_Hz = 0
k_Hz = inf
epsr = 1
tau = 0
RQ = 0

[boundary]
type = PEC

[frequency_info]
; fmin/fmax are DECIMAL EXPONENTS (10^fmin .. 10^fmax), not frequencies in Hz.
; fstep is the number of points per decade exponent.
fmin = 3
fmax = 9
fstep = 2

[beam_info]
gammarel = 7460.52
test_beam_shift = 0.001

; --- the sections below are what makes the file runnable with -a ---

[output]
; which impedances to compute; anything absent or False is skipped
ZLong = True
ZTrans = True
ZLongSurf = True

[output1]
; allowed extensions: .txt, .csv, .dat, .xlsx
output_name = out/arc_chamber.xlsx
; prepend component_name to each column label
use_name_flag = True
output_list = ZLong, ZTrans, ZLongSurf
re_im_flag = both

[img_output1]
img_name = out/arc_chamber_long.png
use_name_flag = False
imped_list = ZLong
re_im_flag = both
title = Longitudinal impedance
; lin | log | symlog
xscale = log
yscale = lin
```

Minimal end-to-end check:

```bash
python -m pytlwall -a examples/ex_run_exec/ex_lowbeta.cfg
```

This writes `low_beta.xlsx`, `low_beta_long.txt` and `low_beta_long.png`
into `examples/ex_run_exec/`.

---

## Testing

The test suite lives in `tests/` and is run with pytest.

```bash
# Install the test dependencies (pytest, pytest-cov)
pip install -e ".[test]"

# Run the whole suite
pytest
```

Expected result on a clean checkout:

```
362 passed, 3 skipped, 40 subtests passed
```

The three skips are expected: `tests/test_cfgio_realistic.py` contains cases
that require the fixture files `test_round.cfg` and `test_rect.cfg`, which are
not distributed with the repository. Anything other than a skip is a genuine
failure.

Coverage is enabled by default through `[tool.pytest.ini_options]` in
`pyproject.toml`: a summary is printed to the terminal and a browsable HTML
report is written to `htmlcov/index.html`. Both `.coverage` and `htmlcov/`
are excluded from version control.

### Running a subset

```bash
# One file
pytest tests/test_tlwall.py

# One test
pytest tests/test_tlwall.py::TestTlWall::test_calc_ZLong

# Verbose, stop at the first failure
pytest -v -x

# Skip the coverage report (faster)
pytest --no-cov
```

### Headless machines

`tests/test_plot.py` builds Matplotlib figures. On a machine without a
display, force a non-interactive backend:

```bash
MPLBACKEND=Agg pytest
```

### Test documentation

Individual test modules are documented under `tests/doc/`, starting from
[TESTING.md](tests/doc/TESTING.md) and [tests_README.md](tests/doc/tests_README.md);
see for example [test_cfg.md](tests/doc/test_cfg.md) and
[test_tlwall_wake.md](tests/doc/test_tlwall_wake.md).

---

## Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| `error: externally-managed-environment` | System Python is protected (PEP 668); create a virtual environment: `python3 -m venv .venv && source .venv/bin/activate` |
| `python: command not found` | On Debian/Ubuntu use `python3`, or activate a virtual environment |
| Import error | Ensure pytlwall is installed: `pip install -e .` |
| `No module named pytlwall` after cloning | Run `pip install -e .` from inside the cloned `pytlwall` directory |
| GUI not launching | Install PyQt5: `pip install pyqt5` |
| Plot not showing | Install Matplotlib: `pip install matplotlib` |
| Batch run prints only the help text | The first argument must be `-a`, `-i`, `--gui` or a `.cfg` path |
| Batch run produces no files | The `.cfg` has no `[output]` / `[outputN]` / `[img_outputN]` sections |
| Excel export fails | Install openpyxl and pandas: `pip install openpyxl pandas` |
| Output written to an unexpected directory | Relative paths follow the working directory unless `[path_info] main_path` is set |
| Config file error | Check INI format and section names |

### Getting Help

1. Check the [API Reference](doc/API_REFERENCE.md)
2. Review the [Examples](examples/README.md)
3. Contact the authors

---

## License

Copyright CERN. All rights reserved.

---

## Version History

- **v2.0** (December 2025)
  - Complete Python refactoring
  - Modern type hints and documentation
  - Qt-based GUI with multi-chamber support
  - MultipleChamber for lattice processing
  - Comprehensive test suite

- **v1.0** (Original)
  - Initial Fortran/Python implementation

---

*Last updated: December 2025*
