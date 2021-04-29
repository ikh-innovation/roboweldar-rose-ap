import os
import sys
from config import ROOT_DIR
sys.path.append(os.path.join(ROOT_DIR, "src", "roboweldar_networking", "interfaces"))
from roboweldar_networking.interfaces.template import send_dummy_files, get_mesh_files, \
    get_trajectory_file


def threedee_reconstruction():
    # send robot pose and photo data to roboweldar-coordinator REST API which then signals a WS message to
    # roboweldar-3d-reconstruction service to fetch these files and start computations. 
    send_dummy_files(endpoint="cache_images", host="localhost",
        path_to_files=os.path.join(ROOT_DIR, "test", "example_files", "raw"))

    # roboweldar-3d-reconstruction should produce a 3D model expressed in the world/robot frame (a.k.a. the
    # transformed mesh) This mesh file (transformed_mesh.obj) will be uploaded to the
    # roboweldar-rose-ap/docker/roboweldar-networking/mesh/ dir.

    # To fetch it via the API, use the following command:
    # get_mesh_files(host, httpPort, path_to_dir, mesh_files)

if __name__ == "__main__":
    threedee_reconstruction()
