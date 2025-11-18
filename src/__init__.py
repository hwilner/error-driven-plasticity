"""
Error-Driven Plasticity Framework
Nature Neuroscience Paper 2 - Computational Analysis

This package implements the multi-scale analysis framework for testing
error-driven plasticity relationships across behavioral, network, synaptic,
and molecular scales of neural organization.

Key Components:
- allen_data_access: Real biological parameter analysis
- enhanced_real_analysis: Multi-scale correlation framework  
- figure_generation: Publication-quality visualizations
- statistical_validation: Bootstrap and robustness testing

Author: [Author Name]
Contact: [Email]
License: MIT with academic citation requirement
Version: 1.2.0 (Nature Neuroscience submission ready)

Citation:
[Author]. Error-Driven Plasticity: A Unified Framework for Learning 
and Adaptation in Neural Circuits. Nature Neuroscience. [DOI when published]

Repository: https://github.com/[username]/error-driven-plasticity-paper2
"""

__version__ = "1.2.0"
__author__ = "[Author Name]"
__email__ = "[author@institution.edu]"
__license__ = "MIT"

# Import main analysis classes
from .allen_data_access import AllenDataProcessor

# Package metadata
__all__ = [
    "AllenDataProcessor",
    "__version__",
    "__author__",
    "__license__"
]

# Ensure reproducibility
import numpy as np
np.random.seed(42)  # Default seed for package-wide reproducibility