# Face recognition on raspberry pi
Installation and demo guide

## Dependencies
Install required libraries with these commands:
```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install build-essential \
    cmake \
    gfortran \
    git \
    wget \
    curl \
    graphicsmagick \
    libgraphicsmagick1-dev \
    libatlas-base-dev \
    libavcodec-dev \
    libavformat-dev \
    libboost-all-dev \
    libgtk2.0-dev \
    libjpeg-dev \
    liblapack-dev \
    libswscale-dev \
    pkg-config \
    python3-dev \
    python3-numpy \
    python3-pip \
    zip
sudo apt-get clean
```

## Installation
Install `face_recognition`:
```
$ pip3 install dlib
$ pip3 install face_recognition
```
## Run 
```
$ python3 face_rec_rpi.py
```

