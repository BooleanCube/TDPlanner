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
- Open a terminal and install the application by cloning the repository into a specific directory
```console
$ git clone https://github.com/BooleanCube/TDPlanner.git
```
- Running `python3 main.py` gets the job done, but by making `main.py` executable with `sudo chmod +x main.py`, you can run the application with `./main.py` without having to call python.
- Creating a desktop profile is convenient but optional.

## Install Latest Stable Release of TDPlanner
- Select the latest release from the [releases page](https://github.com/BooleanCube/TDPlanner/releases) <br>
- Download the `.zip` file. <br>
- Extract the folder and cd into the folder to see its contents. <br>
- Make the `tdplanner` file executable using
```console
$ chmod +x tdplanner
```
- Run the `tdplanner` file to open/start the application using:
```console
$ ./tdplanner
```

## Install matplotlib and PyQt5 (only in some cases)
If the few steps above didn't work for you, the issue probably lies with the matplotlib package not being installed. <br>
Based on how `pip` is setup on your computer run one of the two commands to install matplotlib and retry running `tdplanner`
```console
$ pip install matplotlib
$ pip install pyqt5
```
or
```console
$ python3 -m pip install matplotlib
$ python3 -m pip install pyqt5
```

## Creating a desktop profile for the application (optional for application integration)

### Debian
- Create a `TDPlanner.desktop` in the `Desktop/` folder and put this configuration code within the file:
```desktop
[Desktop Entry]
Name=TDPlanner
Version=v1.0.1
Icon=tdplanner
X-Icon-Path=/path/to/icon/file/
Exec=./path/to/py/file/main.py
Terminal=false
Comment=To Do List Planner Application for Productivity
Type=Application
```
- In the terminal set the permissions of the desktop file to be executable by typing this: `sudo chmod u+x path/to/py/file/main.py`
- Right click on the new empty document and in the Permissions tab, set the execute to allow executing file as program

### Arch
- Make sure the script is executable by running: `sudo chmod +x path/to/py/file/main.py`
- Create a symlink to the script in `/usr/bin/` and make it executable by running the chmod command again.
- Create a `TDPlanner.desktop` in the `/home/.local/share/applications/` folder and put this configuration code within the file:
```desktop
[Desktop Entry]
Name=TDPlanner
Version=v1.0.1
Icon=tdplanner
X-Icon-Path=/path/to/icon/file/
Exec=./path/to/py/file/main.py
Terminal=false
Comment=To Do List Planner Application for Productivity
Type=Application
```
