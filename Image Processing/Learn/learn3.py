import numpy as np
import cv2

# cap = cv2.VideoCapture('videoname') #for video format
cap = cv2.VideoCapture(0) #for single camera

while True:
    ret, frame = cap.read() #displaying video capture  device
    width = int(cap.get(3))
    height = int(cap.get(4))

    image = np.zeros(frame.shape, np.uint8)
    smaller_frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5) #Mirroring Video Multiple Times
    # image[:height//2, :width//2] = cv2.rotate(smaller_frame, cv2.ROTATE_180)
    image[:height//2, :width//2] = smaller_frame
    image[height//2:, :width//2] = smaller_frame
    # image[:height//2, width//2:] = cv2.rotate(smaller_frame, cv2.ROTATE_180)
    image[:height//2, width//2:] = smaller_frame
    image[height//2:, width//2:] = smaller_frame

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

