FROM nvcr.io/nvidia/pytorch:25.01-py3

# Set work directory for build operations
WORKDIR /tmp

# Install system dependencies for libaio (needed for linker)
RUN apt-get update && apt-get install -y --no-install-recommends \
    libaio-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip install --upgrade pip

# Install ipywidgets to fix the tqdm warning
RUN pip install --upgrade ipywidgets jupyter

# Install factory-sdk
RUN pip install factory-sdk

# Fix the flash-attention issue
RUN pip uninstall -y flash-attn
RUN pip install flash-attn --no-build-isolation

# Create non-root user
RUN useradd -m factory

WORKDIR /home/factory

USER factory

COPY ./docker/deployment/run.py /home/factory/run.py

CMD ["python", "/home/factory/run.py"]