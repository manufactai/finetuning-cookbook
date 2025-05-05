FROM nvcr.io/nvidia/pytorch:25.01-py3

#install the factory-sdk
RUN pip install factory-sdk

#non-root user
RUN useradd -m jupyter

#switch to non-root user
USER jupyter

WORKDIR /home/jupyter

#copy notebook into the container
COPY ./notebooks /home/jupyter/finetuning-cookbook/notebooks

#run the notebook
CMD [ "jupyter lab --ip=0.0.0.0 --port=8888 --no-browser" ]