# pytlwall
## Table of contents
 - [Introduction](#introduction)
 - [Installation](#installation)
 - [Tasks performed by pytlwall](#tasks-performed-by-pytlwall)
 - [Structure of the package](#structure-of-the-package)
 - [Installation code](#installation-code)
 - [References](#references)

## Introduction
"pytlwall" is a CERN python code which use the transmission line theory to calculate the resistive wall impedance.
The first version of pytlwall has been made in 2011 in matlab by Carlo Zannini, in 2013
started the python developement.
The current pytlwall version has undergone a major restyling to follow current CERN guidelines and pep8 recommendations.

The aim of the pytlwall is to calculate
- the longitudinal impedance
- the transverse impedance
- the driving and detuning impedance taking care of the form factors (yokoya form factors)
- the space charge impedance (for speed < c)
- the surface impedance

The transmission line equations can be applied recursively to take into account whatever number of layers.
The beam speed and the roughness are taken into account in the formulas.

It is also possible to calculate the impedance of a list of chambers to "build" an entire accelerator.

## Installation
```bash
pip install pytlwall
```
assuming that the package has been downloaded in the current folder.

## Tasks performed by pytlwall


## Structure of the package

```pytlwall``` has the structure used for standard python packages. It consists in a folder named after the package "pytlwall" (which is also the top level of the git repository) 
that contains the source code, the required code and information for the installation, documentation, unit tests and usage examples. In particular:
 - The **source code** is contained in a subfolder that also has the same name of the python package (pytlwall).
 - **Unit tests** is contained in the folder "tests" 
 - **Examples** illustrating the package usage are hosted in the folder "examples"
 - **License** information is contained in the file "LICENSE.txt"
 - This **documentation** is contained in the file "README.md"
 - The **installation process** is defined by the files ["pyproject.toml"](#pyprojecttoml), ["MANIFEST.in"](#manifestin), and  ["setup.py"](#setuppy), which will be described in more detail in the following section.
 


## References
The following resources were used for preparing this package and documentation.



