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
RUN useradd -m jupyter

# Copy notebook into the container
COPY ./notebooks /home/jupyter/finetuning-cookbook/notebooks

# Set proper permissions
RUN chown -R jupyter:jupyter /home/jupyter

# Create jupyter config directory 
RUN mkdir -p /home/jupyter/.jupyter

# Create config file to override defaults
RUN echo "c.ServerApp.root_dir = '/home/jupyter/finetuning-cookbook/notebooks'" > /home/jupyter/.jupyter/jupyter_server_config.py
RUN echo "c.ServerApp.notebook_dir = '/home/jupyter/finetuning-cookbook/notebooks'" >> /home/jupyter/.jupyter/jupyter_server_config.py
RUN chown -R jupyter:jupyter /home/jupyter/.jupyter

# Switch to non-root user
USER jupyter

# Set working directory
WORKDIR /home/jupyter/finetuning-cookbook/notebooks

# Run the notebook
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser"]