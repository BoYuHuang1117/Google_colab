# -*- coding: utf-8 -*-

## Check the GPU selection (T4 or P100 is better)
!/user/local/cuda/bin/nvcc --version
!nvidia-smi

### Reference:
#### https://github.com/Tianxiaomo/pytorch-YOLOv4/blob/master/Use_yolov4_to_train_your_own_data.md
#### https://robocademy.com/2020/05/01/a-gentle-introduction-to-yolo-v4-for-object-detection-in-ubuntu-20-04/#Testing_YOLO_v4_in_a_single_image
#### https://jason-chen-1992.weebly.com/home/-google-colab-yolov41303994
#### https://jason-chen-1992.weebly.com/home/-google-colab-yolov4

## Step 1: Download the darknet repo
!git clone https://github.com/AlexeyAB/darknet

## Step 2: Change parameters and execute
%cd darknet
!sed -i 's/GPU=0/GPU=1/' Makefile
!sed -i 's/OPENCV=0/OPENCV=1/' Makefile
!sed -i 's/CUDNN=0/CUDNN=1/' Makefile
!sed -i 's/CUDNN_HALF=0/CUDNN_HALF=1/' Makefile

!make

## Step 3: Download the neural network structure and corresponding weights
download = True;

if download:
  # download weights from official
  !wget https://pjreddie.com/media/files/yolov3.weights
  !wget https://pjreddie.com/media/files/darknet53.conv.74
  !wget https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v3_optimal/yolov4.weights
  !wget https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v3_optimal/yolov4.conv.137

## Step 4: Run and display the result
def imgShow(path):
  import cv2
  from google.colab.patches import cv2_imshow
  img = cv2.imread(path)
  cv2_imshow(img)

# run darknet detection
!./darknet detect cfg/yolov3.cfg yolov3.weights data/person.jpg

imgShow("predictions.jpg")

# run darknet detection
!./darknet detect cfg/yolov4.cfg yolov4.weights data/dog.jpg

imgShow('predictions.jpg')

## Step 5: zip the network into drive 
from google.colab import drive
drive.mount('/content/gdrive', force_remount=True)

!ln -s /content/gdrive/My\ Drive/yolo_v3v4/ /dir

%cd ..
!zip -r darknet.zip darknet

!cp darknet.zip /dir/darknet.zip

