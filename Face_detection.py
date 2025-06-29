import cv2 
 
# Load the Haar cascade for face detection 
haar_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml File path") 
 
# Initialize the camera (0 for default camera, 1 for external camera) 
cam = cv2.VideoCapture(0) 
 
while True:  # Infinite loop 
    # Read a frame from the camera 
    ret, img = cam.read() 
 
    # Check if the frame was captured correctly 
    if not ret: 
        print("Failed to grab frame") 
        break 
 
    # Convert the color image to grayscale 
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
 
    # Detect faces in the image 
    faces = haar_cascade.detectMultiScale(gray_img, scaleFactor=1.3, minNeighbors=4) 
 
    # Draw rectangles around the detected faces 
    for (x, y, w, h) in faces: 
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 4) 
 
    # Display the frame with detected faces 
    cv2.imshow("Face Detection", img) 
 
    # Check for the escape key (ASCII value 27) 
    key = cv2.waitKey(10) 
    if key == 27:  # Escape key to exit 
        break 
 
# Release the camera and close all OpenCV windows 
cam.release() 
cv2.destroyAllWindows()
