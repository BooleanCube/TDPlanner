# Installation Instructions

## Install TKinter GUI toolkit

### Debian
```console
$ sudo apt install python-tk
```

### Arch
```console
$ sudo pacman -S python-tk
```

## Install Latest Release of TDPlanner
Select the latest release from the [releases page](https://github.com/BooleanCube/TDPlanner/releases) <br>
Download the `.zip` file. <br>
Extract the folder and cd into the folder to see its contents. <br>
Make the `tdplanner` file executable using
```console
$ chmod +x tdplanner
```
Run the `tdplanner` file to open/start the application using:
```console
$ ./tdplanner
```

## Install matplotlib (only in some cases)
If the few steps above didn't work for you, the issue probably lies with the matplotlib package not being installed. <br>
Based on how `pip` is setup on your computer run one of the two commands to install matplotlib and retry running `tdplanner`
```console
$ pip install matplotlib
```
or
```console
$ python3 -m pip install matplotlib
```
