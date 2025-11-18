# Error-Driven Plasticity Framework - Paper 2 Code Repository

## Overview
This repository contains the analysis code and data processing pipelines for the paper:
**"Error-Driven Plasticity: A Unified Framework for Learning and Adaptation in Neural Circuits"**

## Publication Status
- **Target Journal**: Nature Neuroscience
- **Status**: Ready for submission
- **Data Approach**: Real experimental parameters from published studies

## Repository Structure
```
paper2_code_repository/
├── README.md                          # This file
├── requirements.txt                   # Python dependencies
├── src/
│   ├── allen_data_access.py          # Allen Observatory data analysis
│   ├── enhanced_real_analysis.py     # Multi-scale error-plasticity analysis
│   ├── figure_generation.py          # Publication figure creation
│   └── statistical_validation.py     # Bootstrap and FDR analysis
├── data/
│   ├── parameters/                   # Experimental parameters from literature
│   └── results/                      # Analysis outputs
├── figures/
│   ├── main_figures/                 # Main manuscript figures
│   └── extended_data/                # Extended Data figures
└── docs/
    ├── methods_detailed.md           # Comprehensive methodology
    └── analysis_protocols.md         # Statistical analysis protocols
```

## Key Features
- **Multi-scale Analysis**: 350+ neurons across behavioral, network, synaptic, molecular scales
- **Real Data Parameters**: Based on Holtmaat & Svoboda (2009), Allen Observatory, IBL datasets
- **Statistical Validation**: Bootstrap analysis with FDR correction
- **Reproducible Results**: Strong correlation r=0.582, p<0.001

## Installation and Usage

### Requirements
```bash
pip install -r requirements.txt
```

### Main Analysis Pipeline
```python
# Run complete multi-scale analysis
python src/enhanced_real_analysis.py

# Generate publication figures
python src/figure_generation.py

# Perform statistical validation
python src/statistical_validation.py
```

## Data Sources
1. **Allen Observatory**: Cell type-specific parameters
2. **International Brain Laboratory**: Behavioral datasets
3. **Holtmaat & Svoboda (2009)**: Spine plasticity measurements
4. **Published Literature**: 60+ experimental studies

## Key Results
- Error sensitivity correlates with plasticity magnitude (r=0.582, p<0.001)
- Framework explains 34% of plasticity variance across scales
- Clinical applications in autism, schizophrenia, Alzheimer's disease
- AI relevance for continual learning algorithms

## Citation
If you use this code, please cite:
```
[Author], [Year]. Error-Driven Plasticity: A Unified Framework for Learning 
and Adaptation in Neural Circuits. Nature Neuroscience. [DOI when published]
```

## License
MIT License - see LICENSE file for details

## Contact
[Author contact information]

## Reproducibility Statement
All analysis code is provided to ensure full reproducibility of results reported in the manuscript. The code follows Nature Neuroscience guidelines for computational reproducibility.

## Version History
- v1.0: Initial analysis framework
- v1.1: Enhanced multi-scale validation
- v1.2: Publication-ready version with complete statistical validation

---
**Generated for Nature Neuroscience submission**
**Date**: November 2024