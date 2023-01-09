# cuda image
FROM tensorflow/tensorflow:2.11.0-gpu-jupyter
WORKDIR /workspace
COPY requirements.txt /tmp/requirements.txt
RUN apt-get update & apt-get install -y git
RUN pip install --upgrade pip
RUN pip install -r /tmp/requirements.txt
RUN pip install torch torchvision torchaudio

# create vscode user
RUN useradd -ms /bin/bash vscode
USER vscode
#add vscode to sudoers
USER root
RUN apt-get update && \
      apt-get -y install sudo

RUN adduser vscode sudo
# set password for user vscode
RUN echo "vscode:pass" | chpasswd

######
# Install prerequisites for psycopg2
RUN apt-get update && apt-get install -y \
    python-dev \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install wget
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends wget

#Install make
RUN apt install build-essential -y --no-install-recommends


# Install miniconda

RUN echo ${ARCHITECTURE}
ENV CONDA_DIR /opt/conda
###TODO: /bin/bash: /root/miniconda.sh: No such file or directory
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh && \
    /bin/bash ~/miniconda.sh -b -p $CONDA_DIR && \
    rm ~/miniconda.sh && \
    $CONDA_DIR/bin/conda clean -ya
ENV PATH=$CONDA_DIR/bin:$PATH




#switch back to vscode user
USER vscode

RUN pip install -U ipykernel

#RUN echo "conda activate base" >> ~/.bashrc
#SHELL ["/bin/bash", "--login", "-c"]
# COPY /home/jtito/code/wib-ai/experiments/jtito/torch-nilm/torch-nilm.yml /workspaces/environment.yml
# RUN conda env create -f /workspaces/environment.yml
# RUN echo "conda activate torch-nilm" >> ~/.bashrc
# SHELL ["/bin/bash", "--login", "-c"]