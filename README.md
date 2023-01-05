# crystal_kernel

<p align="center"><img src="https://user-images.githubusercontent.com/5798442/183279700-0f61d484-9460-4802-9c1b-5e6b07b5e1a5.png"></p>

[![PyPI Version](https://img.shields.io/pypi/v/crystal-kernel.svg)](https://pypi.org/project/crystal-kernel/)
[![License](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)

Simple [Python wrapper kernel](https://jupyter-client.readthedocs.io/en/stable/wrapperkernels.html) for Crystal language.
[ICrystal](https://github.com/RomainFranceschini/icrystal) is the widely used Jupyter kernel for Crystal, 
which uses [ICR](https://github.com/crystal-community/icr). 
On the other hand, this crystal_kernel uses the official [Crystal interpreter](https://crystal-lang.org/2021/12/29/crystal-i.html).

Forked from [bash_kernel](https://github.com/takluyver/bash_kernel)

## Installation

Make sure the [Crystal's interpreter](https://crystal-lang.org/2021/12/29/crystal-i.html) starts with `crystal i`. 

Then type the following commands.

```sh
pip install crystal_kernel

python -m crystal_kernel.install
```

## Compiling Crystal interpreter

Crystal 1.3.2 does not provide the Crystal interpreter by default. 

To enable `crystal i`, you need to [compile Crystal from source code](https://crystal-lang.org/install/from_sources/) with `interpreter` option. Crystal is required to compile Crystal. So please do not remove the existing Crystal just because you are going to install Crystal from source code.

```sh
git clone https://github.com/crystal-lang/crystal
cd crystal
make help                               # check available options
make interpreter=1 release=1 progress=1 # whatever you want
sudo make install                       # sudo checkinstall
```

Then check the interpreter start.

```sh
crystal i
```

Did it work?

## Using Shards

Use shards when you want to use crystal libraries. Go to your working directory and create `shard.yml` with `shards init` and write the necessary libraries to it. After `shards install`, start `jupyter`.

## Development

* See [Python wrapper kernel](https://jupyter-client.readthedocs.io/en/stable/wrapperkernels.html).
* Something is better than nothing.

Feel free to fork this project and start your own project. The author (kojix2) is not familiar with Python and is ready to transfer this project to a more suitable person. If you are interested in taking over the project, please let us know.
