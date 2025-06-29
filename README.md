Real-Time Face Detection Using OpenCV

This project demonstrates real-time face detection using Haar Cascades with OpenCV and Python.
It captures video from your webcam, detects faces in real time, and draws rectangles around them.

Features

- Real-time video capture from webcam  
- Face detection using Haar Cascade classifier  
- Visual feedback with rectangle overlays  

Requirements

- Python 3.11  
- OpenCV (`cv2`)  
- Haar Cascade XML file for face detection

Setup Instructions

1. Install Dependencies

   Make sure you have Python 3.11 installed. Then, install OpenCV:

   ```bash
   pip install opencv-python
   ```

2. Download Haar Cascade File

   Download the `haarcascade_frontalface_default.xml` and save it to your desired path.

3. Code Setup

   Replace the path in the following line with the location of your downloaded XML file:

   ```python
   haar_cascade = cv2.CascadeClassifier("path/to/haarcascade_frontalface_default.xml")
   ```

4. Camera Note

   - Use cv2.VideoCapture(0) for default (internal) webcam

   - Use cv2.VideoCapture(1) for external USB camera

How to Run

```bash
python face_detection.py
```

Press Esc (Escape key) to exit the webcam preview window.

Demo

This project captures real-time video, detects faces, and highlights them with red rectangles.
