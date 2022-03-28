# crystal_kernel

<img alt="Crystal" src="https://crystal-lang.org/assets/media/crystal_logo.svg" height="100"></img>
<img alt="Jupyter" src="https://docs.jupyter.org/en/latest/_static/jupyter.svg" height="50"></img>

[![PyPI Version](https://img.shields.io/pypi/v/crystal-kernel.svg)](https://pypi.org/project/crystal-kernel/)

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
sudo make install                       # sudo checkinstall (I am a fan of checkinstall)
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

