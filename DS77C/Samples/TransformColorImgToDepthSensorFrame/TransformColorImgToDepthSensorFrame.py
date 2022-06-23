from pickle import FALSE, TRUE
import sys
sys.path.append('../../../')

from DS77C.API.VzenseDS77C_api import *
import time

camera = VzenseTofCam()


camera_count = camera.VZ_GetDeviceCount()
retry_count = 100
while camera_count==0 and retry_count > 0:
    retry_count = retry_count-1
    camera_count = camera.VZ_GetDeviceCount()
    time.sleep(1)
    print("scaning......   ",retry_count)

device_info=VzDeviceInfo()

if camera_count > 1:
    ret,device_infolist=camera.VZ_GetDeviceInfoList(camera_count)
    if ret==0:
        device_info = device_infolist[0]
        for info in device_infolist: 
            print('cam uri:  ' + str(info.uri))
    else:
        print(' failed:' + ret)  
        exit()  
elif camera_count == 1:
    ret,device_info=camera.VZ_GetDeviceInfo()
    if ret==0:
        print('cam uri:' + str(device_info.uri))
    else:
        print(' failed:' + ret)   
        exit() 
else: 
    print("there are no camera found")
    exit()

if  VzConnectStatus.Connected.value != device_info.status:
	print("connect statu:",device_info.status)  
	print("Call VZ_OpenDeviceByUri with connect status :",VzConnectStatus.Connected.value)
	exit()
else:
    print("uri: "+str(device_info.uri))
    print("alias: "+str(device_info.alias))
    print("connectStatus: "+str(device_info.status))

ret = camera.VZ_OpenDeviceByUri(device_info.uri)
if  ret == 0:
    print("open device successful")
else:
    print('VZ_OpenDeviceByUri failed: ' + str(ret))   

ret = camera.VZ_StartStream()
if  ret == 0:
    print("start stream successful")
else:
    print("VZ_StartStream failed:",ret)     

 
# set Mapper
ret = camera.VZ_SetTransformColorImgToDepthSensorEnabled(c_bool(True))

if  ret == 0:
    print("set DepthToRGB")
else:
    print("VZ_SetMapperEnabledDepthToRGB failed:",ret)     

while 1:
    ret, frameready = camera.VZ_GetFrameReady(c_uint16(80))
    if  ret !=0:
        print("VZ_GetFrameReady failed:",ret)
        time.sleep(1)
        continue       

    if  frameready.transformedColor:      
        ret,frame = camera.VZ_GetFrame(VzFrameType.VzTransformColorImgToDepthSensorFrame)
        if  ret == 0:
            curPath = os.getcwd()
            print (curPath)
            folder = curPath+ "/save"
            if not os.path.exists(folder):
                print("not exists")
                os.makedirs(folder)
            else:
                print("already exists")
            filename = folder + "/transformedColor.bin"
            file = open(filename,"wb+")
            for i in range(frame.dataLen):
                file.write(c_uint8(frame.pFrameData[i]))
                
            print("save ok")
            break
        else:   
            print("mappeddepth  error:",ret)  
ret = camera.VZ_StopStream()       
if  ret == 0:
    print("stop stream successful")
else:
    print('VZ_StopStream failed: ' + str(ret))  

ret = camera.VZ_CloseDevice()     
if  ret == 0:
    print("close device successful")
else:
    print('VZ_CloseDevice failed: ' + str(ret))   
           