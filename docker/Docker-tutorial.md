# Docker tutorial

## 1. Installation

## On Windows
Install [WSL](https://docs.microsoft.com/it-it/windows/wsl/install-win10)

Install [linux kernel](https://aka.ms/wslstore) (open microsoft store and install ubuntu)

Install [Docker Desktop](https://docs.docker.com/docker-for-windows/install/)

## On Ubuntu
Uninstall older versions:
```
sudo apt-get remove docker docker-engine docker.io containerd runc
```
Set up the repository
```
sudo apt-get update
```
```
sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
```
Add Docker’s official GPG key:
```
 curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
```
```
echo \
  "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```
Install Docker Engine
```
sudo apt-get update
```
```
sudo apt-get install docker-ce docker-ce-cli containerd.io
```

Verify that Docker Engine is installed correctly by running the hello-world image.
```
 sudo docker run hello-world
```

Now we have Docker installed.

## 2. Make a Docker image
Let's make a Docker image of a little python project. In this case we want to make an image containing a python code that plots the Mandelbrot set.

To make an image, we have to write a configuration file, named literally *Dockerfile*. In this file we will add the files that we want to put inside the image and run bash commands.

![](img/dir.png)

To do this, go to the directory of your python project, and open a text file named Dockerfile. In my case the environment of the Docker image will be python, but can be also Ubuntu, Apline, etc.
Then, we have to add the files that we need for the code, so the python files (mandelbrot.py, utils.py) and also the requirements files. To add them we have to write `ADD mandelbrot.py /`. The final slash means the position of the filesystem of the container. We could also write `ADD mandelbrot.py /home/me/Desktop`, and docker will create these directories in the container and will put these files in that directories.

Then we add also the requirements file to install all the dependencies of the source code.
In fact, after adding it, we can install the dependencies using the command `RUN pip install -r requirements.txt`.

After that, we can run the source code with the command `CMD [ "python", "mandelbrot.py" ]`. And the container will run the source code.
At the end my Dockerfile will have this form:
```
FROM python:3

ADD mandelbrot.py /
ADD utils.py /
ADD requirements.txt /

RUN pip install -r requirements.txt

CMD [ "python", "mandelbrot.py" ]
```
But this is only a configuration file, the image is not yet created. We need to *build* it, and to do this we have to run:
```
docker build -t mandelbrot .
```
where `-t` means tag, which refers to `mandelbrot` which is the name I want to give to the image, and the dot means the path where to look for the files.

After the build, we can check the presence of the built image with the command:
```
docker images
```
```
Output:
REPOSITORY   TAG       IMAGE ID       CREATED             SIZE
mandelbrot   latest    4ac354bc4ef6   About a minute ago   1.05GB

```

Now we can run the container:
```
docker run mandelbrot
```
```
Output:
Hi from the docker container!
```

## Input files and results

Now, if we have a project with some output files like plots or tabular data, we have to add volumes to the container. this is so because the docker container have a close and indipendent filesystem, and if we want to have access to this file system, we have to create mount points.

To do this, we have to run the command:
```
docker run -v /path/to/wanted/results/:/path/to/results/inside/the/container/ mandelbrot
```
So in my case for example:
```
docker run -v /home/riccardo/Desktop/:/results/ mandelbrot
```

This is the same for the input files: if we have some input data to give to the code, we have to mount the directory in which we have the data.

Note that in the source code I had to save the plot of the mandelbrot set in the directory results:

```
plt.savefig("results/mandelbrot.png")
```

which refers to the filesystem of the container.

## DockerHub

Like GitHub where we store repositories and source codes, we can store docker images on a web service, [DockerHub](https://hub.docker.com/)

We can have an account and different repositories, public or private.


## Connect Docker with GitHub
Suppose we have a python project in a github repository, and you want to make this package available to others. To make sure that other users can run the code without dependencies problems, we can make a docker image. So we add to the github repository a Dockerfile which can automatically build an image on dockerhub in a specific repository.
To do so, we have firstly to connect dockerhub with github, see https://docs.docker.com/docker-hub/builds/link-source/

Next, we have to add a yaml file to our github repository in order to run GitHub Actions.
To do so, go to your repository on github and go to `Actions`:

![](img/action.png)

Then, click on `New Workflow` and (in my case) then on ` set up a workflow yourself `.

It will automatically open a yaml file in which we can insert all the steps of our worklow. In my case, I want to publish on my DockerHub account a new image of my project, so I wrote:
```
name: Publish Docker image
on:
  release:
    types: [published]
jobs:
  push_to_registry:
    name: Push Docker image to Docker Hub
    runs-on: ubuntu-latest
    steps:
      - name: Check out the repo
        uses: actions/checkout@v2
      - name: Log in to Docker Hub
        uses: docker/login-action@v1
        with:
          username: ${{ secrets.DOCKER_USERNAME }}
          password: ${{ secrets.DOCKER_PASSWORD }}
      - name: Push to Docker Hub
        uses: docker/build-push-action@v2
        with:
          push: true
          tags: riccardoscheda/mandelbrot:latest
```
What we need are the credentials for the dockerhub account (`secrets.DOCKER_USERNAME` and `secrets.DOCKER_PASSWORD`), and also the name of the repository where we want to publish our image.
Firstly, to add the credentials on github, go to the settings of the repository:

![](img/secrets.png)

Then we create one secret for the username `DOCKER_USERNAME` and one secret for the password `DOCKER_PASSWORD`.

Ok, now we have to create the repository of the project on DockerHub, in my case I created a repository `mandelbrot`, and in the last line of the yaml file you can see `riccardoscheda/mandelbrot:latest`.

Now we are ready; when we create a new Release of our github project:

![](img/rel1.png)
![](img/rel2.png)
![](img/rel3.png)

Now if we publish this release, we can check the build in `Actions` section:

![](img/rel4.png)

When the building is finished, we can see our published image on DockerHub:

![](img/dockerhub.png)


# Using Docker containers with the gpu
Before you get started, make sure you have installed the NVIDIA driver for your Linux distribution.
Then, follow these istructions taken from [NVIDIA](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#docker)
```
distribution=$(. /etc/os-release;echo $ID$VERSION_ID) \
   && curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add - \
   && curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list
```

```
sudo apt-get update
```

```
sudo apt-get install -y nvidia-docker2
```
```
sudo systemctl restart docker
```


```
sudo docker run --rm --gpus all nvidia/cuda:11.0-base nvidia-smi
```

Then when you run your docker image, use the command:

```
docker run <image> --gpus all
```
