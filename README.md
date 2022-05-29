# files-gitpod

Meltano project [file bundle](https://meltano.com/docs/command-line-interface.html#file-bundle) for [Gitpod](https://www.gitpod.io/)

_Note: This file-bundle is functional but is still Beta. Its intended for local instances only. Please test it out and provide feedback, contributions are always welcome too!_

This plugin will add the following files to your Meltano project:

- `.gitpod.yml`
- `.gitpod/Dockerfile`
- `.gitpod/docker-compose.yml`

## Installation

To install the Gitpod file bundle into your Meltano project you need to use a custom file bundle.

```
# Add Gitpod files to your Meltano project
meltano add --custom files gitpod
```
