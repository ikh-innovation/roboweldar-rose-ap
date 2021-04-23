import send_dummy_files from http_client

# TODO: refactor

# TODO: mention the ./setup.sh for CUDA in documentation

def main():
    # send robot pose and photo data to roboweldar-coordinator REST API which then signals a WS message to roboweldar-3d-reconstruction 
    # service to fetch these files and start computations.
    # TODO: path_to_files shoudl equal "test/example_files/raw dir"
    send_dummy_files(endpoint="cache_images", host="localhost", path_to_files)

    # roboweldar-3d-reconstruction should produce a 3D model expressed in the world/robot frame (a.k.a. the transformed mesh)
    # This mesh file (transformed_mesh.obj) will be uploaded to the roboweldar-rose-ap/docker/roboweldar-networking/mesh/ dir. 

    # To fetch it via the API, use the following command:
    get_mesh_files(host, httpPort, path_to_dir, mesh_files)

    # The transformed mesh file can be uploaded to the roboweldar-weld-seam-detection service via the roboweldar-coordinator REST API
    # For that, we can signal a WS message via the httpServer.weldSeamDetectionStartEndpoint method, which instructs the 
    # roboweldar-weld-seam-detection to download the transformed mesh file and run computations on it. Once it finishes, it uploads
    # the result to the coordinator's welding_trajectory/ dir.
    
    # To download it, we can either check the dir, or use the GET request of the coordinator API to download it:
    get_trajectory_file()


if __name__ == "__main__":
    main()
