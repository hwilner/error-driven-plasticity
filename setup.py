#!/usr/bin/env python3
"""
Setup script for Error-Driven Plasticity Framework
Nature Neuroscience Paper 2 - Computational Analysis Package
"""

from setuptools import setup, find_packages
import os

# Read README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read requirements
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

# Package metadata
setup(
    name="error-driven-plasticity",
    version="1.2.0",
    author="[Author Name]",
    author_email="[author@institution.edu]",
    description="Multi-scale analysis framework for error-driven synaptic plasticity",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/[username]/error-driven-plasticity-paper2",
    project_urls={
        "Bug Tracker": "https://github.com/[username]/error-driven-plasticity-paper2/issues",
        "Documentation": "https://github.com/[username]/error-driven-plasticity-paper2/blob/main/README.md",
        "Source Code": "https://github.com/[username]/error-driven-plasticity-paper2",
        "Paper": "[DOI when published]"
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Information Analysis",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=3.0.0", 
            "black>=22.0.0",
            "flake8>=4.0.0",
            "mypy>=0.950"
        ],
        "docs": [
            "sphinx>=4.5.0",
            "sphinx-rtd-theme>=1.0.0",
            "nbsphinx>=0.8.0"
        ],
        "analysis": [
            "jupyter>=1.0.0",
            "jupyterlab>=3.0.0",
            "ipywidgets>=7.6.0"
        ]
    },
    entry_points={
        "console_scripts": [
            "error-plasticity-analysis=src.allen_data_access:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.md", "*.txt", "*.yml", "*.yaml"],
    },
    keywords=[
        "neuroscience", 
        "plasticity", 
        "synapses", 
        "prediction errors", 
        "learning",
        "computational biology",
        "systems neuroscience",
        "brain modeling"
    ],
    license="MIT",
    zip_safe=False,
)

# Post-installation message
print("\n" + "="*60)
print("ERROR-DRIVEN PLASTICITY FRAMEWORK INSTALLED")
print("="*60)
print("Version: 1.2.0 (Nature Neuroscience submission)")
print("Repository: https://github.com/[username]/error-driven-plasticity-paper2")
print("\nQuick Start:")
print("  python -c \"from src.allen_data_access import AllenDataProcessor; proc = AllenDataProcessor()\"")
print("\nDocumentation:")
print("  See README.md and docs/ directory")
print("\nCitation:")
print("  [Author]. Error-Driven Plasticity: A Unified Framework.")
print("  Nature Neuroscience. [DOI when published]")
print("="*60 + "\n")