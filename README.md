# YBCO Reproducibility Framework: Application of Clinical Trial-Inspired Methodology to High-Tc Superconductivity

**Author**: Bleu Radiance  
**Date**: December 27, 2025  

## Overview
This repository expands the clinical trial-inspired framework (from LENR work) to YBa₂Cu₃O₇-δ (YBCO) superconductivity. It includes Tc simulations with mathematical variants (noise, broader dome, inhomogeneous doping) to address reproducibility challenges and doping gaps.

Key: Parabolic Tc model, sensitivity analysis, and phased protocol for synthesis/validation.

## Citation
[![DOI](https://zenodo.org/badge/DOI/[YOUR_NEW_DOI].svg)](https://doi.org/[YOUR_NEW_DOI])  

Bleu Radiance (2025). YBCO Reproducibility Framework. Zenodo. https://doi.org/[YOUR_NEW_DOI]

## Files
- `manuscript.md`: Full theoretical paper.
- `ybco_tc_simulation.py`: Reproducible Python code for Tc vs δ simulations (run with `python ybco_tc_simulation.py`).
- `PROTOCOL.md`: Experimental protocol for YBCO testing.
- `figures/`: Generated plots (e.g., Tc model and sensitivity).
- `LICENSE`: MIT (code), CC-BY-4.0 (manuscript).

## Quick Start
```bash
git clone https://github.com/BleuRadiance/ybco-reproducibility-framework.git
cd ybco-reproducibility-framework
python ybco_tc_simulation.py  # Runs simulations, prints outputs, saves plots
