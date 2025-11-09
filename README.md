#  Ball Detection and Tracking (SportVot AI Assignment)

##  Overview
This project detects and tracks a moving ball in sports videos using YOLOv11 for detection and SORT for object tracking.

##  Tech Stack
- Python, OpenCV, NumPy
- YOLOv11 (Ultralytics)
- SORT Algorithm (Tracking)

##  Features
- Custom ball dataset trained using YOLOv11
- Real-time detection and tracking with bounding boxes and IDs
- Output video saved automatically (`results/tracked_output.mp4`)

## Model Performance
- **Precision:** 0.90  
- **mAP@50:** 0.47  
- **Recall:** 0.31


##  Demo
The video file `tracked_output.mp4` shows real-time tracking results.  
Download dataset and model weights from ( https://universe.roboflow.com/computer-vision-d3h0p/custom-ball-annotation)

##  How to Run
```bash
pip install ultralytics opencv-python numpy
python track.py


---



