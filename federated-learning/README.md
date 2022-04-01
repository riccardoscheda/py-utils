# Federated learning

## Python libraries

There are many ways to do federated learning, mainly due to different libraries.
The mainly ways i found are:

- NVIDIA Clara [link](https://developer.nvidia.com/clara)

  Not seen yet deeply
- Huawei MindSpore [link](https://github.com/mindspore-ai/mindspore)

  Even the installation is difficult
- PySyft (I prefer this) [link](https://github.com/OpenMined/PySyft)

  this seems to be the most easy to use. This is an example for using real devices: [federated learning](https://blog.openmined.org federated-learning-of-a-rnn-on-raspberry-pis/)

- Tensorflow federated [link](https://www.tensorflow.org/federated)

  I tried many times to follow the tutorial but never managed to do a real example with different devices.

## Server and client tools

These libraries also use different ways to connect servers and clients:

- mlsocket `pip install mlsocket`
- grpc (used by tensorflow) [installation](https://grpc.io/docs/languages/python/quickstart/)
- PySyft (used by PyTorch) [https://github.com/OpenMined/PySyft]()
