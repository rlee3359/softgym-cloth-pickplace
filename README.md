# SoftGym Cloth PickPlace
This is a fork of <a href="https://sites.google.com/view/softgym/home">SoftGym</a>, reduced and modified specifically for table top pick place of cloth, with a visual actionspace normalized 0-1. Specifically, the environment was modified to remove the white/gray background rendering, remove rendering of gripper spheres, and improved the pick-place actionspace for top down fold actions. The path the gripper takes between the pick and place points is modified for improved folds.

## Using Docker
If you are using Ubuntu 16.04 LTS and CUDA 9.2, you can follow the steps in the next section on this page for compilation. For other versions of Ubuntu or CUDA, we provide the pre-built Docker image and Dockerfile for running SoftGym. Please refer to our [Docker](docker/docker.md) page.

## Instructions for Installation
1. This codebase is tested with Ubuntu 16.04 LTS, CUDA 9.2 and Nvidia driver version 440.64. Other versions might work but are not guaranteed, especially with a different driver version. Please use our docker for other versions.

The following command will install some necessary dependencies.
```
sudo apt-get install build-essential libgl1-mesa-dev freeglut3-dev libglfw3 libgles2-mesa-dev
```

2. Create conda environment
   Create a conda environment and activate it: `conda env create -f environment.yml`

3. Compile PyFleX: Go to the root folder of softgym and run `. ./prepare_1.0.sh`. After that, compile PyFleX with CMake & Pybind11 by running `. ./compile_1.0.sh` Please see the example test scripts and the bottom of `bindings/pyflex.cpp` for available APIs.

## Environment
This fork only contains a single cloth environment for pick and place folding from an above view camera.
Actions are normalized to 0-1.

![0a](https://user-images.githubusercontent.com/15622840/186578438-e59002b0-6909-4819-a6a8-f04a43a47f6f.png)
![0n](https://user-images.githubusercontent.com/15622840/186578441-e0cf7f56-93b6-42bb-be79-dc5f5c6e52e6.png)

## Example
The script "human_demo_example.py" provides a simple example of usage and a user interface for click-drag pick and place action demonstration.

```
python human_demo_example.py
```


## Cite
If you find this codebase useful in your research, please consider citing:
```
@inproceedings{corl2020softgym,
 title={SoftGym: Benchmarking Deep Reinforcement Learning for Deformable Object Manipulation},
 author={Lin, Xingyu and Wang, Yufei and Olkin, Jake and Held, David},
 booktitle={Conference on Robot Learning},
 year={2020}
}
```

## References
- NVIDIA FleX - 1.2.0: https://github.com/NVIDIAGameWorks/FleX
- Our python interface builds on top of PyFleX: https://github.com/YunzhuLi/PyFleX
- If you run into problems setting up SoftGym, Daniel Seita wrote a nice blog that may help you get started on SoftGym: https://danieltakeshi.github.io/2021/02/20/softgym/
