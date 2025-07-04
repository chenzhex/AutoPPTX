# setup.py kept for compatibility. See pyproject.toml for full config.

from setuptools import setup, find_packages
import os

# Read long description from README.md
long_description = (
    open("README.md", encoding="utf-8").read()
    if os.path.exists("README.md") else ""
)

setup(
    name="autopptx",
    version="0.1.0",
    description="A Python tool for automated editing of PowerPoint templates using python-pptx",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Chenzhe",
    author_email="chenzhe0_0@163.com",
    maintainer="Chenzhe",
    maintainer_email="chenzhe0_0@163.com",
    url="https://github.com/chenzhex/AutoPPTX",
    license="MIT",
    packages=find_packages(where="autopptx"),
    package_dir={"": "autopptx"},
    include_package_data=True,
    install_requires=[
        "python-pptx>=1.0.2",
        "lxml>=5.3.1"
    ],
    python_requires=">=3.10",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Topic :: Office/Business :: Presentation",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords=[
        "powerpoint",
        "automation",
        "presentation",
        "python-pptx",
        "template",
    ],
    project_urls={
        "Homepage": "https://github.com/chenzhex/AutoPPTX",
        "Documentation": "https://github.com/chenzhex/AutoPPTX#readme",
        "Repository": "https://github.com/chenzhex/AutoPPTX",
        "Issues": "https://github.com/chenzhex/AutoPPTX/issues",
    },
)