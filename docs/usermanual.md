# User Manual

## Example

### Directory structure

The directory `test/example_files` contains the following folders:

- `raw`: this folder contains a number of photographs taken around the periphery of a steel welding target. For each image, it also contains the corresponding robot pose (in the world frame) at the time the photograph was taken, in `.npy` format. A human readable `poses.txt` file is included, where each row corresponds to a flattened augmented rotation matrix of 12 elements (9 rotation values, 3 position values). The `camera.yaml` file contains the camera intrinsics.

- `cameras`: After the completion of `StructureFromMotion` node in AliceVision Meshroom a `cameras.sfm` file is produced. Inside this file all the views' instrics and extrinsics are listed. Under the `poses` keyword we can find the views' poses. This particular `cameras.sfm` file, is the result of running the default photogrammetry pipeline on the photographs in the `raw` folder.

- `output`: This folder contains the subfolders `mesh` and `transformed_mesh`. `mesh` is the standard output of the photogrammetry pipeline, while `transformed_mesh` is the output of the transformation pipeline. Both folders contain `.mtl`, `.obj` and `.png` files.


### Running the example


First, make sure you have installed the docker Nvidia driver:

```bash
cd docker
sudo chmod a+x docker_cuda_install_script.sh
./docker_cuda_install_script.sh
```

Then, we set up the services by starting our docker containers. Run

```bash
sudo chmod a+x entrypoint.sh
./entrypoint.sh
```

This will create folders in the `docker` dir, which allow you to peek into each container's state. This is helpful because you may want to manually inspect files, or copy them over to your host manually. Now that the services are up and running, we can move on to interacting with them.

From the repository root, run

```bash
cd src
python3.7 -m virtualenv .venv
source .venv/bin/activate
pip install -r roboweldar_networking/interfaces/requirements.txt
```

Now you should have the required packages installed in the Python venv on your host, so that you can proceed with running the example. In the same terminal, run 

```bash
python example.py
```

TODO: Need to finalize `example.py` and then write some more documentation.