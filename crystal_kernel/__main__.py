from ipykernel.kernelapp import IPKernelApp
from .kernel import CrystalKernel

IPKernelApp.launch_instance(kernel_class=CrystalKernel)
