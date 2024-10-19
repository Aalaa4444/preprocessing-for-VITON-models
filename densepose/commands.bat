@echo off
cd /d D:\blackboard\GP\FR\SD-VITON\data\WinDensePose-master
cd cocoapi\PythonAPI
python setup.py build
python setup.py install
cd ..\..\densepose
python setup.py build
python setup.py install
cd ..
setpath.bat
cd densepose
python tools\infer_simple.py --cfg configs\DensePose_ResNet101_FPN_s1x-e2e.yaml --output-dir DensePoseData\infer_out\ --image-ext jpg --wts https://dl.fbaipublicfiles.com/densepose/DensePose_ResNet101_FPN_s1x-e2e.pkl DensePoseData\demo_data\00006_00.jpg
pause
