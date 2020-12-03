# Install CUDA, cudaToolkit and CuDNN 

For explanations see the guide:
[](https://medium.com/@stephengregory_69986/installing-cuda-10-1-on-ubuntu-20-04-e562a5e724a0)

## 1. Clean up
```
sudo rm /etc/apt/sources.list.d/cuda*
sudo apt remove --autoremove nvidia-cuda-toolkit
sudo apt remove --autoremove nvidia-*
```

```
sudo apt-get purge nvidia*
sudo apt-get autoremove
sudo apt-get autoclean
```

```
sudo rm -rf /usr/local/cuda*
```

## 2. Install

```
sudo apt update
sudo add-apt-repository ppa:graphics-driverssudo apt-key adv --fetch-keys http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/7fa2af80.pubsudo bash -c 'echo "deb http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64 /" > /etc/apt/sources.list.d/cuda.list'sudo bash -c 'echo "deb http://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64 /" > /etc/apt/sources.list.d/cuda_learn.list'
```

NOTICE this is for cuda 10.1, but there should be latest versions

```
sudo apt update
sudo apt install cuda-10-1
sudo apt install libcudnn7
```

## 3. Add CUDA to PATH

Open:

```
sudo gedit ~/.profile
```
Add this to the end of the file:
```
# set PATH for cuda 10.1 installation
if [ -d "/usr/local/cuda-10.1/bin/" ]; then
    export PATH=/usr/local/cuda-10.1/bin${PATH:+:${PATH}}
    export LD_LIBRARY_PATH=/usr/local/cuda-10.1/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
fi
```

## 4. Reboot

## 5. Final Check
```
nvidia-smi
```
Check CUDA:
```
nvcc --version
```
Check CuDNN:
```
/sbin/ldconfig -N -v $(sed ‘s/:/ /’ <<< $LD_LIBRARY_PATH) 2>/dev/null | grep libcudnn
```
