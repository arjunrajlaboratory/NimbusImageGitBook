---
description: How to install NimbusImage
---

# Installation

If you really want to install NimbusImage yourself, you can :). Before getting into the details of installation, it's important to understand the structure of NimbusImage. The front end and back end are two completely independent components. The web application lives on the front end, while all your data and analyses reside in the back end. You can mix and match almost any front end with any back end. For example, you could use nimbusimage.com for the front end and run the back end on your local laptop or vice versa. We here provide instructions for installing both, but again, the easiest option is to simply use the online version.

A good halfway point (if you must) is to use the front end provided by nimbusimage.com along with your own back end. That way, your data lives on your own computer, in case that is important to you.

## Installing the back end

The back end is a data management system called [Girder](https://girder.readthedocs.io/en/latest/), which is developed by Kitware. You can install it fairly easily using Docker. Keep in mind that Docker on Mac is really slow for various reasons, so we strongly recommend using Linux. Also, some workers that require GPUs, like cellpose for cell segmentation, need a Linux system with a GPU.

To install the backend, first you need to install Docker.

**Linux:**

1. **I**nstall using the apt-repository. Follow [these instructions](https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository). Then follow these [post-install instructions](https://docs.docker.com/engine/install/linux-postinstall/).
2. If you want to use GPU workers, you will need to [install CUDA](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html). Make sure your GPU driver is installed (probably need 535 or higher).&#x20;
3. Then install the Nvidia [Docker toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html).
4. Wasn't that easy? I hate Linux. Also, you will probably have to restart your computer at least once by now.

**Mac:**

1. Install using the [Docker app](https://docs.docker.com/desktop/install/mac-install/).

**Now install the backend using Docker:**

* Pull the NimbusImage repository to install Girder:

```
git clone https://github.com/kitware/UPennContrast
cd UPennContrast/
docker compose build
docker compose up -d
```

* Pull the worker repository to install workers:

```
git clone https://github.com/arjunrajlab/ImageAnalysisProject
chmod +x build_machine_learning_workers.sh
chmod +x build_workers.sh
./build_machine_learning_workers.sh
./build_workers.sh
```

You should now be able to see the backend at [http://localhost:8080](https://localhost:8080). You can login with login "admin" and password "password". **We strongly recommend changing those defaults ASAP!**

## Installing the front end

To install the frontend, you need to:

1. Install [node.js](https://nodejs.org/en/download/package-manager/current).
2.  Pull the repository (if you haven't already):

    ```
    git clone https://github.com/kitware/UPennContrast
    cd UPennContrast/
    ```
3.  Run the following commands:

    ```
    npm install
    npm run emscripten-build
    ```
4.  If you are on Linux, you may need to run:

    ```
    cat /proc/sys/fs/inotify/max_user_watches
    sudo sysctl fs.inotify.max_user_watches=1000000
    sudo sysctl -p
    ```
5.  Copy in the models for Segment Anything (optional):

    ```
    smkdir -p UPennContrast/public/onnx-models/sam/vit_b
    cd UPennContrast/public/onnx-models/sam/vit_b
    wget "https://huggingface.co/rajlab/sam_vit_b/resolve/main/decoder.onnx" -O decoder.onnx
    wget "https://huggingface.co/rajlab/sam_vit_b/resolve/main/encoder.onnx" -O encoder.onnx
    ```
6. Now start up the server:
   1.  If you want to run the development build:

       ```
       npm run dev
       ```
   2.  If you want to run for production:

       ```
       npm run build
       npm run serve
       ```
7. You should see a bunch of things, including somewhere "localhost:8081" or "localhost:5173"
8. Go to http://localhost:8081 or http://localhost:5173 and you should see the website! Be sure to set your Girder domain to http://localhost:8080 when you are logging in:

## Sign in (if you are running your own server)

Navigate to a NimbusImage server like [nimbusimage.org](https://nimbusimage.org/). Use your login credentials from above as follows:

1. **In the "Girder domain" field, enter the domain associated with your account.** This will probably be `https://nimbusimage.org/girder`.
2. **Enter your username and password.** Note that this username and password is associated with the Girder domain above.

<figure><img src=".gitbook/assets/image (21).png" alt="" width="365"><figcaption></figcaption></figure>
