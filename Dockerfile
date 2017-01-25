FROM ubuntu:16.04

# Install OpenCV
RUN apt-get update \
  && apt-get install -y build-essential cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev python3 python3-pip python3.5-dev wget unzip python3-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev \
  && cd /opt \
  && wget https://github.com/Itseez/opencv/archive/3.1.0.zip \ 
  && unzip 3.1.0.zip \
  && cd opencv-3.1.0 \
  && mkdir build \
  && cd build \
  && cmake -D CMAKE_BUILD_TYPE=Release -D CMAKE_INSTALL_PREFIX=/usr/local .. \
  && make -j7 \
  && make install \
  && cd .. \
  && rm -rf build \
  && apt-get remove -y unzip wget \
  && pip3 install scikit-image scipy beautifulsoup4 requests mahotas

CMD /bin/bash