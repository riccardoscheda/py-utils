# OpenCV Install

First of all, install [Python3](install-conda.sh) and [CMake](install-cmake.md)
Instructions to install OpenCV from source on Ubuntu 20.04

```
sudo apt update
sudo apt upgrade
```

After that, install `g++` and `gcc` and boost library

```
sudo apt install -y gcc-8 g++-8
sudo apt install libboost-all-dev
```

and OpenCV required repository

```
sudo apt install -y libpng-dev libtiff-dev libgtk2.0-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libgtk2.0-dev libatlas-base-dev gfortran webp zlib1g-dev qt5-default libvtk6-dev
```

create the installation directory and clone `opencv` and `opencv_contrib` repository

```
mkdir opencv_build
cd opencv_build
git clone https://github.com/opencv/opencv.git
git clone https://github.com/opencv/opencv_contrib.git
```

to install an older than latest version, enter the two directory and type the command `git checkout opencv-version`

Once the download is completed:

```
cd opencv
mkdir -p build && cd build
```

set-up the opencv build with cmake:

```
cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D INSTALL_C_EXAMPLES=ON \
    -D INSTALL_PYTHON_EXAMPLES=ON \
    -D OPENCV_GENERATE_PKGCONFIG=ON \
    -D OPENCV_EXTRA_MODULES_PATH=~/opencv_build/opencv_contrib/modules \
    -D BUILD_EXAMPLES=ON ..
```

and start the compilation and installation, modify the `-j` flag based on the number of core / threads of your processor.

```
make -j12
sudo make install
ldconfig
```

To verify the installation:

```
pkg-config --modversion opencv4
python -c "import cv2; print(cv2.__version__)"
```

Both should give as output the version OpenCV you chose.
