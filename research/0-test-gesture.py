import cv2
from pyfirmata import Arduino, util
import modules.finger_distancer as FingerDistancer

# OpenCV setup
cap = cv2.VideoCapture(0)

# Main loop
while cap.isOpened():
    ret, frame = cap.read()

    # Call the function from the module
    frame, speed = FingerDistancer.main_process(frame)

    # Display the frame
    cv2.imshow("Display", frame)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
