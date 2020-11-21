# CMake Install

There are pre-compiled binary at the [download page](https://cmake.org/download/).
Or, if you want to build from source:

```
wget https://github.com/Kitware/CMake/releases/download/v3.19.0/cmake-3.19.0.tar.gz
tar xzf cmake-3.19.0.tar.gz
```

where 3.19.0 can be replaced with the version you want.
Then:

```
cd cmake-3.19.0
./bootstrap
make
make install
```
