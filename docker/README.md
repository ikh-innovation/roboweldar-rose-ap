# README.md for DockerHub

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

## How to run the component instance

The [Compose](docker-compose.yml) file associated with this repository can
be invoked to run the component in the following way:

```console
sudo chmod +x entrypoint.sh
./entrypoint.sh
```

The `entrypoint.sh` script sets up the docker volumes which you can use to peek inside the containers' data directories, and successively runs
This [Compose](docker-compose.yml) file defines three services: The [server module](https://github.com/ikh-innovation/roboweldar-networking/tree/master/server), the [3D reconstruction module](https://github.com/ikh-innovation/roboweldar-3d-reconstruction), and the [weld seam detection module](https://github.com/ikh-innovation/roboweldar-weld-seam-detection).

The server module is instantiated by pulling an image that’s built from the Dockerfile in the `server` directory of the respective repository, using the integration pipeline from Dockerhub. It then binds the container and the host machine to the exposed port, 3000 (HTTP) and 3001 (Websocket).
The same is valid for the 3D reconstruction module and the weld seam detection module.

## Building the images locally

If you would like the [Compose](docker-compose.yml) file to use locally built images of the above modules, you may opt to build them yourself. Docker build instructions are found in each respective repository.

- [Server docker instructions](https://github.com/ikh-innovation/roboweldar-networking/blob/master/server/README.md)
- [3D reconstruction  docker instructions](https://github.com/ikh-innovation/roboweldar-3d-reconstruction/blob/master/docker/README.md)
- [Weld seam detection docker instructions](https://github.com/ikh-innovation/roboweldar-weld-seam-detection/blob/master/docker/README.md)
