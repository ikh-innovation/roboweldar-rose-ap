# <TITLE>

[![License: MIT](https://img.shields.io/github/license/ramp-eu/TTE.project1.svg)](https://opensource.org/licenses/MIT)
[![Docker badge](https://img.shields.io/docker/pulls/ramp-eu/TTE.project1.svg)](https://hub.docker.com/r/<org>/<repo>/)
<br/>
[![Documentation Status](https://readthedocs.org/projects/tte-project1/badge/?version=latest)](https://tte-project1.readthedocs.io/en/latest/?badge=latest)
[![CI](https://github.com/ramp-eu/TTE.project1/workflows/CI/badge.svg)](https://github.com/ramp-eu/TTE.project1/actions?query=workflow%3ACI)
[![Coverage Status](https://coveralls.io/repos/github/ramp-eu/TTE.project1/badge.svg?branch=master)](https://coveralls.io/github/ramp-eu/TTE.project1?branch=master)
[![Codacy grade](https://img.shields.io/codacy/grade/99310c5c4332439197633912a99d2e3c)](https://app.codacy.com/manual/jason-fox/TTE.project1)
[![CII Best Practices](https://bestpractices.coreinfrastructure.org/projects/4187/badge)](https://bestpractices.coreinfrastructure.org/projects/4187)

```text

The Badges above demonstrate testing, code coverage
and commitment to coding standards (since the code is linted on commit).

The links need to be amended to point to the correct repo.

Sign up for:

- CI Test system - e.g. GitHub Actions, Travis
- A Documentation website - e.g. ReadTheDocs
- Static Code Analysis tool - e.g. Codacy
- CII Best Practices https://bestpractices.coreinfrastructure.org

Only CII Best Practices (and its badge) is mandatory. Any equivalent public automated tools for the other three may be used.

Note that the CII Best Practices questionaire will request evidence of tooling used.

```

```text
This repository contains the source code to the RoboWeldAR ROSE-AP module. Given a set of photographs of a metallic object destined for welding, this module produces 3D-reconstructed model of that object, along with proposed welding paths.
```

This project is part of [DIH^2](http://www.dih-squared.eu/). For more information check the RAMP Catalogue entry for the
[components](https://github.com/xxx).

| :books: [Documentation](https://tte-project1.readthedocs.io/en/latest/) | :whale: [Docker Hub](https://hub.docker.com/r/link-to-docker) |
| --------------------------------------------- | ------------------------------------------------------------- |


## Contents

-   [Background](#background)
-   [Install](#install)
-   [Usage](#usage)
-   [API](#api)
-   [Testing](#testing)
-   [License](#license)

## Background


The ROSE-AP building block is one of the functional cores of the RoboWeldAR system (along with the robotic control module), and encapsulates the 3D reconstruction and weld seam detection components.

![High-level architecture](rose-ap-arch.jpg)

- Inputs: An array of photos from different angles, camera pose for each photo 

- Outputs: 3D reconstructed object, welding trajectories (paths and poses) that represent where welding targets should be welded and how they should be approached. 

- Description: The most time-consuming part of the RoboWeldAR workflow is the 3-D reconstruction, which is why in our implementation we have developed a logger which broadcasts updates to the Orion Context Broker in NGSIv2 format, so that the user can monitor the progress. This ROSE-AP will be of interest to manufacturing entities that already use robotic welding processes in their workflow. The only modification to the hardware required is the addition of an off-the-shelf RGB camera, and a way to collect robot pose for each photograph capture so that it can be provided to the ROSE-AP component. After the output is produced and sent back to the end user, the end user must provide a way to provide the produced welding trajectory to their robot. As long as the robot frame has not been translated or rotated between the photo capture and welding processes, the welding trajectory will remain valid and ready for utilization. 


## Install

```text
How to install the component

Information about how to install the <Name of component> can be found at the corresponding section of the
[Installation & Administration Guide](docs/installationguide.md).

A `Dockerfile` is also available for your use - further information can be found [here](docker/README.md)

```

## Usage

```text
How to use the component

Information about how to use the <Name of component> can be found in the [User & Programmers Manual](docs/usermanual.md).

The following features are listed as [deprecated](docs/deprecated.md).
```

## API

```text
Definition of the API interface:

Information about the API of  the <Name of component> can be found in the [API documentation](docs/api.md).

```

## Testing

```text
How to test the component

For performing a basic end-to-end test, you have to follow the step below. A detailed description about how to run tests can be found [here].

> npm test

```

## License

[MIT](LICENSE) © <TTE>
