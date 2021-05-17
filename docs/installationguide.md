# Installation Guide

To run the component instance, we recommend a Linux installation (preferably Ubuntu 18.04 or above), and the latest versions of Docker and Docker Compose. You will make sure to have a CUDA-compatible graphics card installed on your system, and the proprietary NVIDIA graphics drivers. Below you can find the steps required to get the dependencies installed before you attempt to run the instance.

## Docker installation instructions

For best results, we recommend installing everything on a Linux machine, preferably Ubuntu 20, or another Debian-based Linux distribution. Prior to running the component, you must have Docker and Docker Compose installed on your host. It is recommended to download the latest versions using [these](https://docs.docker.com/engine/install/ubuntu/) and [these](https://docs.docker.com/compose/install/) instructions respectively.

*Note*: the component was tested using the following versions:

- docker: `Docker version 20.10.6, build 370c289`
- docker-compose: `docker-compose version 1.29.1, build c34c88b2`

## NVIDIA CUDA installation instructions

### CUDA Toolkit

While the containers are CUDA-enabled themselves, you will have to ensure that you have a working installation of the [CUDA Toolkit](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html) on your system. After installation, the output of command `nvidia-smi` should produce something similar to this:

```console
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 460.27.04    Driver Version: 460.27.04    CUDA Version: 11.2     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  GeForce GT 710      Off  | 00000000:08:00.0 N/A |                  N/A |
| 42%   46C    P0    N/A /  N/A |    732MiB /  1993MiB |     N/A      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+
                                                                               
+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
|  No running processes found                                                 |
+-----------------------------------------------------------------------------+
```

If not, make sure you followed the installation steps correctly, and that you have a [CUDA-enabled GPU](https://developer.nvidia.com/cuda-gpus) installed on your host.

### NVIDIA Container Toolkit

In order for the container instances to get access to the NVIDIA CUDA driver on the host, we need to install the `nvidia-docker2` package, which is described [here](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html). For this, we can run the following:

```console
sudo chmod +x docker_cuda_install_script.sh
./docker_cuda_install_script.sh
```

*Note*: the component was tested using the following versions:

- cuda: `11.2`
- driver version: `460.27.04`
