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

* Pull the NimbusImage repository:

```sh
git clone https://github.com/arjunrajlaboratory/NimbusImage.git
cd NimbusImage/
```

* Start docker images for the backend:

```sh
docker compose build
docker compose up -d
```

You should now be able to see the backend at [http://localhost:8080](https://localhost:8080). You can login with login "admin" and password "password". **We strongly recommend changing those defaults ASAP!**

## Installing the workers

Go to a **new directory** (NOT the `NimbusImage` directory) and run the following:

```sh
git clone https://github.com/arjunrajlab/ImageAnalysisProject
cd ImageAnalysisProject/
chmod +x build_machine_learning_workers.sh
chmod +x build_workers.sh
./build_machine_learning_workers.sh
./build_workers.sh
```

The machine learning workers will run on CPU on Linux if a GPU is not available, although will run much more slowly.

## Installing the front end

To install the frontend, you need to:

1. Install [node.js](https://nodejs.org/en/download/package-manager/current).
2. Install [pnpm](https://pnpm.io/installation):
   ```sh
   npm i -g pnpm
   ```
3. Pull the repository (if you haven't already done so for the backend):

    ```sh
    git clone https://github.com/arjunrajlaboratory/NimbusImage.git
    cd NimbusImage/
    ```
4. Install node modules:

    ```sh
    pnpm install
    ```
5. Compile C++ code to wasm:
    ```sh
    pnpm emscripten-build
    ```
6.  If you are on Linux, you may need to run:

    ```sh
    cat /proc/sys/fs/inotify/max_user_watches
    sudo sysctl fs.inotify.max_user_watches=1000000
    sudo sysctl -p
    ```
7.  Copy in the models for Segment Anything (optional):

    ```sh
    mkdir -p public/onnx-models/sam/vit_b
    cd public/onnx-models/sam/vit_b
    wget "https://huggingface.co/rajlab/sam_vit_b/resolve/main/decoder.onnx" -O decoder.onnx
    wget "https://huggingface.co/rajlab/sam_vit_b/resolve/main/encoder.onnx" -O encoder.onnx
    cd ../../../.. # Go back to the NimbusImage root directory
    ```
8. Now start up the server:
   1.  If you want to run the development build:

       ```sh
       pnpm run dev
       ```
       You should see output indicating the server is running, likely on `http://localhost:5173`.
   2.  If you want to run for production:

       ```sh
       pnpm build
       pnpm run serve
       ```
       You should see output indicating the server is running, likely on `http://localhost:4173`.
9. Go to the relevant localhost URL (`http://localhost:5173` for dev, `http://localhost:4173` for prod) and you should see the website!

## Sign in (if you are running your own server)

IMPORTANT: By default, an admin user will be created with the login `admin` and the password `password`. You can use these credentials to initially log into the system.

1. Navigate to your running NimbusImage frontend (e.g., `http://localhost:5173`).
2. **In the "Girder domain" field, enter the domain associated with your backend.** If running locally, this will be `http://localhost:8080`.
3. **Enter the username (`admin`) and password (`password`).**
4. **For security, it is critical to add a new admin user in Girder and then remove the original `admin` user.** To do this, go to `http://localhost:8080`, sign into Girder using the default credentials, then go to the `Users` tab on the left to manage users.

<figure><img src=".gitbook/assets/image (21).png" alt="" width="365"><figcaption>Make sure to set the Girder domain to your backend server, e.g., http://localhost:8080</figcaption></figure>
