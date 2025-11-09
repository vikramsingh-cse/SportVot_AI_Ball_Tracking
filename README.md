 Ball Detection & Tracking using YOLOv11 + SORT
(SportVot AI Assignment Project)
 Overview

This project aims to detect and track a sports ball in real-time from videos using YOLOv11 for detection and SORT (Simple Online and Realtime Tracking) for motion tracking.

It demonstrates a full end-to-end workflow — from dataset handling to training, inference, and tracking — built completely in Python.

 Tech Stack
Category	Tools / Frameworks
Programming Language	Python 
Deep Learning Framework	PyTorch (via Ultralytics YOLOv11)
Computer Vision	OpenCV, NumPy
Tracking Algorithm	SORT (Kalman Filter + Hungarian Algorithm)
Visualization	Matplotlib, OpenCV
Dataset Source	Roboflow - Custom Ball Annotation
 Project Workflow

Dataset Collection & Preprocessing

Downloaded and annotated ball images from Roboflow.

Organized into train/, valid/, and test/ folders.

Model Training

Trained YOLOv11 model for 20 epochs on CPU.

Saved trained weights as runs/detect/train3/weights/best.pt.

Inference (Detection)

Detected sports ball in unseen images and videos using trained weights.

Tracking (SORT Algorithm)

Tracked the ball across frames assigning unique IDs to moving objects.

Final tracked output saved as results/tracked_output.mp4.

 Model Performance
Metric	Value
Precision	0.90
Recall	0.31
mAP@50	0.47
mAP@50–95	0.19
 Project Structure
SportVot_AI_Project/
│
├── dataset/
│   ├── train/
│   ├── valid/
│   ├── test/
│   └── data.yaml
│
├── runs/
│   └── detect/
│       └── train3/
│           └── weights/
│               ├── best.pt
│               └── last.pt
│
├── sort.py
├── track.py
├── sample_video.mp4
├── results/
│   └── tracked_output.mp4
└── README.md

🚀 How to Run Locally
#  Clone the repository
git clone https://github.com/<your-username>/SportVot_AI_Ball_Tracking.git
cd SportVot_AI_Ball_Tracking

#  Install dependencies
pip install ultralytics opencv-python numpy filterpy

#  Run the tracker
python track.py


Key Highlights

Custom-trained YOLOv11 model for single-class detection (sports ball)

Real-time multi-object tracking using SORT algorithm

End-to-end modular structure (train, detect, track)

Clean, reproducible implementation

 Dataset & Model

Download dataset and trained model weights here:
Google Drive Link
  https://universe.roboflow.com/computer-vision-d3h0p/custom-ball-annotation


 Author

Vikram Singh Rajput
 Final Year Engineering Student | AI & Full Stack Enthusiast
 Aspiring Software Engineer | Focused on AI & MNC Opportunities
 LinkedIn (https://www.linkedin.com/in/vikramsingh-rajawat/)
 GitHub  (https://github.com/vikramsingh-cse/)

 Acknowledgments

Special thanks to SportVot AI Team for the assignment and the opportunity to apply real-world computer vision techniques in a sports analytics context.






