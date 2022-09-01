#!/bin/bash
FILE=$(realpath "$0")
DIR=$(dirname "${FILE}")
source "${DIR}/utils.sh"

# Initial
printd "Initialize ... " Cy
apt-get update -qqy
apt-get install -qy figlet boxes tree > /dev/null 2>&1
pip3 install --disable-pip-version-check --force pip~=21.0

printd "System Require " Cy
apt-get -qy install bsdmainutils zip jq wget usbutils

# OpenCV
printd "Install OpenCV " Cy
apt-get install -qqy libxrender1 libsm6 libxext6 #> /dev/null 2>&1
pip3 install -q --disable-pip-version-check opencv-python==4.1.2.30 #> /dev/null 2>&1

# TLT Converter
printd "Install Dependencies of TLT Converter " Cy
apt-get install -qqy libssl-dev #> /dev/null 2>&1
echo 'export TRT_LIB_PATH=/usr/lib/x86_64-linux-gnu' >> ~/.bashrc 
echo 'TRT_INC_PATH=/usr/include/x86_64-linux-gnu' >> ~/.bashrc 

# Torch 
printd "Install torch, torchvision with CUDA 11.1 " Cy
pip3 install --disable-pip-version-check torch==1.9.0+cu111 torchvision==0.10.0+cu111 torchaudio==0.9.0 -f https://download.pytorch.org/whl/torch_stable.html

printd "Install other msicellaneous packages " Cy
pip3 install --disable-pip-version-check tqdm cython gdown setuptools packaging pycocotools GPUtil wget colorlog

# For darknet yolo to tensorrt
printd "Install the requirement of Darknet " Cy
pip3 install onnx==1.9.0

# For web api
apt-get -o Dpkg::Options::="--force-confmiss" install --reinstall netbase
pip3 install flask flask-socketio==5.1.2 flask-cors flasgger gunicorn==20.1.0 eventlet==0.30.2
pip3 install python-engineio==4.3.2 python-socketio==5.6.0

# For Package
pip3 install merak pyinstaller

# Clean
apt-get clean

printd "Done${REST}"
