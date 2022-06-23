## Python Wrapper for DS-BaseSDK API

Python wrapper is an opensource project of Vzense TOF camera API.

The goal of this project is to help developers use Vzense TOF camera via python method easily.

- PythonSDK version: V1.0.6
- DS-BaseSDK version: V1.0.6

### Supported Devices

- DS77Lite 
- DS77CLite
- DS77Pro  
- DS77CPro  

### Requirements

- python version : 3.7.x
- python modules : ctypes, numpy, opencv-python(display only)

### Directory

- **DS77**: the API and Sample code for DS77Lite/DS77Pro
- **DS77C**: the API and Sample code for DS77CLite/DS77CPro
- **Lib**: VzenseBaseSDK dynamic library files
- **install.py**: install file
- **config.txt**: set the config that needed by 'install.py', such as:
```
system = Windows64
url = https://gitee.com
```
|system|details|
|---|---|
|Windows64|windows 64 bit|
|Windows32|windows 32 bit|
|Ubuntu20.04|the same with Ubuntu18.04 PC SDK|
|Ubuntu18.04|for PC with x86_64-linux-gnu(v7.5.0)|
|Ubuntu16.04|for PC with x86_64-linux-gnu(v5.4.0)|
|AArch64|for aarch64 with aarch64-linux-gnu(v5.4.0)|
|Arm-linux-gnueabihf|for arm32 with arm-linux-gnueabihf(v5.4.0)|

|url|
|---|
|https://gitee.com|
|https://github.com|

### Quick Start

- step1. install modules:
         
```	 
	  pip install numpy
	  pip install opencv-python 
```
- step2. Set 'config.txt' according to your needs

- step3. Run the 'python install.py' 

- step4. Switch to Samples under the product directory, run the sample that you need. 
    	 
         For example, go to the DS77/Samples/FrameViewer, then run 'python FrameViewer_DS77.py'

