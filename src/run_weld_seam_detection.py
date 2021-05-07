import os
import sys
from config import ROOT_DIR
sys.path.append(os.path.join(ROOT_DIR, "src", "roboweldar_networking", "interfaces"))
from roboweldar_networking.interfaces.template import send_dummy_files, get_mesh_files, \
    get_trajectory_file


def weld_seam_detection():
    # The transformed mesh file can be uploaded to the roboweldar-weld-seam-detection service via the
    # roboweldar-coordinator REST API For that, we can signal a WS message via the
    # httpServer.weldSeamDetectionStartEndpoint method, which instructs the roboweldar-weld-seam-detection
    # to download the transformed mesh file and run computations on it. Once it finishes, it uploads the
    # result to the coordinator's welding_trajectory/ dir.

    # Note: if you haven't run the run_3d_reconstruction.py script first, you will need to 
    # upload the transformed mesh to the coordinator module manually, either via using the REST API,
    # or by copying the example transformed mesh from test/example_files/output/transformed_mesh into 
    # docker/roboweldar-coordinator/mesh

    import requests
    requests.get("http://localhost:3000/start_welding_seam_detection")

    # To download it, we can either check the dir, or use the GET request of the coordinator API to
    # download it: get_trajectory_file()


if __name__ == "__main__":
    weld_seam_detection()
