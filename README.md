# crystal_kernel

<img alt="Crystal" src="https://crystal-lang.org/assets/media/crystal_logo.svg" height="100"></img>
<img alt="Jupyter" src="https://docs.jupyter.org/en/latest/_static/jupyter.svg" height="50"></img>

[![PyPI Version](https://img.shields.io/pypi/v/crystal-kernel.svg)](https://pypi.org/project/crystal-kernel/)

Simple [Python wrapper kernel](https://jupyter-client.readthedocs.io/en/stable/wrapperkernels.html) for Crystal language.
[ICrystal](https://github.com/RomainFranceschini/icrystal) is the widely used Jupyter kernel for Crystal, 
which uses [ICR](https://github.com/crystal-community/icr). 
On the other hand, this crystal_kernel uses the official [Crystal interpreter](https://crystal-lang.org/2021/12/29/crystal-i.html).

Forked from [bash_kernel](https://github.com/takluyver/bash_kernel)

## installation

Make sure the [Crystal's interpreter](https://crystal-lang.org/2021/12/29/crystal-i.html) starts with `crystal i`. 

Then type the following commands.

```
pip install crystal-kernel

git clone https://github.com/kojix2/crystal_kernel
python crystal_kernel/install.py
```

## Development

Something is better than nothing.

