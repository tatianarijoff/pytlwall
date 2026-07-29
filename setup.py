"""
Setup script for pytlwall package.

pytlwall is a Python implementation for calculating resistive wall impedance
using transmission line theory, originally developed at CERN.

This setup includes both the core pytlwall library and the pytlwall_gui
graphical interface.
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read the long description from README
readme_file = Path(__file__).parent / "README.md"
if readme_file.exists():
    long_description = readme_file.read_text(encoding="utf-8")
else:
    long_description = "Transmission line impedance calculation engine"

# Read version from _version.py
version_file = Path(__file__).parent / "pytlwall" / "_version.py"
version = "1.0.0"  # Default
if version_file.exists():
    with open(version_file) as f:
        for line in f:
            if line.startswith("__version__"):
                version = line.split("=")[1].strip().strip('"').strip("'")
                break

#########
# Setup #
#########
setup(
    # Package metadata
    name="pytlwall",
    version=version,
    description="Transmission line impedance calculation engine with GUI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    
    # Author information
    author="Tatiana Rijoff, Carlo Zannini",
    author_email="tatiana.rijoff@gmail.com",
    maintainer="Tatiana Rijoff",
    maintainer_email="tatiana.rijoff@gmail.com",
    
    # URLs
    url="https://github.com/tatianarijoff/pytlwall",
    project_urls={
        "Bug Reports": "https://github.com/tatianarijoff/pytlwall/issues",
        "Source": "https://github.com/tatianarijoff/pytlwall",
        "Documentation": "https://github.com/tatianarijoff/pytlwall/blob/main/README.md",
    },
    
    # License
    license="MIT",
    
    # Classifiers for PyPI
    classifiers=[
        # Development Status
        "Development Status :: 5 - Production/Stable",
        
        # Intended Audience
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        
        # Topic
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Scientific/Engineering",
        
        # License
        "License :: OSI Approved :: MIT License",
        
        # Python versions
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        
        # Operating Systems
        "Operating System :: OS Independent",
        
        # Natural Language
        "Natural Language :: English",
    ],
    
    # Keywords for search
    keywords="impedance, transmission line, accelerator physics, CERN, beam dynamics, GUI",
    
    # Package discovery - include both pytlwall and pytlwall_gui
    packages=find_packages(
        exclude=["tests", "tests.*", "examples", "examples.*", "docs", "docs.*"]
    ),
    
    # Python version requirement
    python_requires=">=3.8",
    
    # Core dependencies (without GUI)
    install_requires=[
        "numpy>=1.20.0",
        "scipy>=1.7.0",
        "matplotlib>=3.3.0",
        "openpyxl>=3.0.0",
    ],
    
    # Optional dependencies
    extras_require={
        # GUI requires PyQt5
        "gui": [
            "PyQt5>=5.15.0",
        ],
        # Development tools
        "dev": [
            "pytest>=7.0",
            "pytest-cov>=3.0",
            "black>=22.0",
            "flake8>=4.0",
            "mypy>=0.950",
            "ruff>=0.1.0",
        ],
        # Documentation
        "docs": [
            "sphinx>=4.0",
            "sphinx-rtd-theme>=1.0",
            "myst-parser>=0.18",
        ],
        # Testing
        "test": [
            "pytest>=7.0",
            "pytest-cov>=3.0",
        ],
        # All optional dependencies
        "all": [
            "PyQt5>=5.15.0",
            "pytest>=7.0",
            "pytest-cov>=3.0",
            "black>=22.0",
            "flake8>=4.0",
            "mypy>=0.950",
            "ruff>=0.1.0",
            "sphinx>=4.0",
            "sphinx-rtd-theme>=1.0",
        ],
    },
    
    # Package data - include Yokoya factors and GUI resources
    include_package_data=True,
    package_data={
        "pytlwall": [
            "yokoya_factors/*.txt",
            "yokoya_factors/*.dat",
            "yokoya_factors/*.csv",
        ],
        "pytlwall_gui": [
            "*.png",
            "*.ico",
            "*.svg",
            "resources/*",
            "logo.png",
        ],
    },
    
    # Entry points for command-line scripts
    entry_points={
        "console_scripts": [
            "pytlwall=pytlwall.__main__:main",
        ],
        "gui_scripts": [
            "pytlwall-gui=pytlwall_gui.main:main",
        ],
    },
    
    # Zip safe
    zip_safe=False,
)
