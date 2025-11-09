from ultralytics import YOLO
import cv2
from sort import Sort
import numpy as np

# Load trained YOLO model
model = YOLO(r"runs\detect\train3\weights\best.pt")

# Initialize tracker
tracker = Sort()

# Load your test video
video_path = r"sample_video.mp4"  # video file in project folder
cap = cv2.VideoCapture(video_path)

# Output setup
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('results/tracked_output.mp4', fourcc, 30.0,
                      (int(cap.get(3)), int(cap.get(4))))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Run YOLO detection
    results = model.predict(frame, conf=0.4, verbose=False)
    detections = []

    for box in results[0].boxes:
        x1, y1, x2, y2 = box.xyxy[0].tolist()
        conf = box.conf[0].item()
        detections.append([x1, y1, x2, y2, conf])

    detections = np.array(detections)
    tracks = tracker.update(detections)

    # Draw tracking boxes
    for track in tracks:
        x1, y1, x2, y2, track_id = map(int, track)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, f'ID {track_id}', (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    out.write(frame)
    cv2.imshow("Tracking", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
print("Tracking complete! Output saved as results/tracked_output.mp4")
