# README.md for DockerHub

## Installation

Please refer [here](https://github.com/ikh-innovation/roboweldar-rose-ap/blob/main/docs/installationguide.md) for installation instructions.

## How to run the component instance

The [Compose](docker-compose.yml) file associated with this repository can
be invoked to run the component in the following way:

```console
sudo chmod +x entrypoint.sh
./entrypoint.sh
```

The `entrypoint.sh` script sets up the docker volumes which you can use to peek inside the containers' data directories, and successively runs `docker-compose.yml`. This [Compose](docker-compose.yml) file defines three services: The [server module](https://github.com/ikh-innovation/roboweldar-networking/tree/master/server), the [3D reconstruction module](https://github.com/ikh-innovation/roboweldar-3d-reconstruction), and the [weld seam detection module](https://github.com/ikh-innovation/roboweldar-weld-seam-detection).

The server module is instantiated by pulling an image that’s built from the Dockerfile in the `server` directory of the respective repository, using the integration pipeline from Dockerhub. It then binds the container and the host machine to the exposed port, 3000 (HTTP) and 3001 (Websocket).
The same is valid for the 3D reconstruction module and the weld seam detection module.

A tutorial on how the component can be used can be found [here](https://github.com/ikh-innovation/roboweldar-rose-ap/blob/main/docs/usermanual.md).

## Where to find the built images

Built images for each dependency can be found on DockerHub:

- [Coordinator Docker](https://hub.docker.com/r/roboweldar/roboweldar-coordinator)
- [3D reconstruction Docker](https://hub.docker.com/r/roboweldar/roboweldar-3d-reconstruction)
- [Weld seam detection Docker](https://hub.docker.com/r/roboweldar/roboweldar-weld-seam-detection)

## Building the images locally

If you would like the [Compose](docker-compose.yml) file to use locally built images of the above modules, you may opt to build them yourself. Docker build instructions are found in each respective repository.

- [Server docker instructions](https://github.com/ikh-innovation/roboweldar-networking/blob/master/server/README.md)
- [3D reconstruction  docker instructions](https://github.com/ikh-innovation/roboweldar-3d-reconstruction/blob/master/docker/README.md)
- [Weld seam detection docker instructions](https://github.com/ikh-innovation/roboweldar-weld-seam-detection/blob/master/docker/README.md)
