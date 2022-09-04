# Image contents:
#     https://github.com/microsoft/vscode-dev-containers/tree/v0.245.2/containers/python-3/.devcontainer/base.Dockerfile
#     https://docs.microsoft.com/en-us/azure/databricks/kb/libraries/install-pygraphviz


# [Choice]
# The available Python versions, use a variant with suffix -bullseye on local arm64/Apple Silicon:
# 3, 3.10, 3.9, 3.8, 3.7, 3.6,
# 3-bullseye, 3.10-bullseye, 3.9-bullseye, 3.8-bullseye, 3.7-bullseye, 3.6-bullseye,
# 3-buster, 3.10-buster, 3.9-buster, 3.8-buster, 3.7-buster, 3.6-buster
ARG VARIANT="3.10-bullseye"
FROM mcr.microsoft.com/vscode/devcontainers/python:0-${VARIANT}


# [Choice]
# The Node.js versions:
# none, lts/*, 16, 14, 12, 10
ARG NODE_VERSION="none"
RUN if [ "${NODE_VERSION}" != "none" ]; then su vscode -c "umask 0002 && . /usr/local/share/nvm/nvm.sh && nvm install ${NODE_VERSION} 2>&1"; fi


# [Optional]
# The pip requirements rarely change, the image set-up is:

# ... installations via requirements.txt
COPY requirements.txt /tmp/app/
RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/app/requirements.txt \
  && rm -rf /tmp/app

# ... graphviz, which dask requires, has to be installed separately
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
  && apt-get -y install python3-dev graphviz libgraphviz-dev pkg-config
RUN pip3 install graphviz
