from setuptools import setup, find_packages

setup(
    name="files-gitpod",
    version="0.1.1",
    description="Meltano project files for gitpod",
    packages=find_packages(),
    package_data={
        "bundle": [
            ".gitpod.yml",
            ".gitpod/Dockerfile",
            ".gitpod/docker-compose.yml",            
        ]
    },
)
