"""
Setup script for ZBIT-CORE-v2
Install with: pip install -e .
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="zbit-core-v2",
    version="2.0.0",
    author="ZBIT Quantum Team",
    author_email="zbit@quantumcore.org",
    description="Scalable Floquet-Topological Quantum Simulation with 3D Tensor Networks and Hybrid QML",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zbit/core-v2",
    project_urls={
        "Bug Tracker": "https://github.com/zbit/core-v2/issues",
        "Documentation": "https://github.com/zbit/core-v2/tree/main/docs",
        "Source Code": "https://github.com/zbit/core-v2",
        "arXiv Paper": "https://arxiv.org/abs/2510.xxxxx",
    },
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Scientific/Engineering :: Quantum Computing",
    ],
    python_requires=">=3.10",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
            "black>=23.9.0",
            "pylint>=2.17.0",
            "mypy>=1.4.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "zbit-demo=zbit_core_v2_FINAL_WORKING:main",
        ],
    },
)
