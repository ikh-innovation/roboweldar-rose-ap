#!/bin/bash

mkdir -p roboweldar-3d-reconstruction
mkdir -p roboweldar-coordinator
mkdir -p roboweldar-weld-seam-detection
chown -R 1000:1000 roboweldar-3d-reconstruction
chown -R 1000:1000 roboweldar-coordinator
chown -R 1000:1000 roboweldar-weld-seam-detection
docker-compose up

