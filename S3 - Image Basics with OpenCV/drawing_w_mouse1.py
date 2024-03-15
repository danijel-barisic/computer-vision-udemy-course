import cv2
import numpy as np


#FUNCTION#
def drawCircle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x,y), 100, (0,255,0),-1)
    
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img, (x,y), 100, (0,0,255),-1)

cv2.namedWindow(winname='my_drawing')

cv2.setMouseCallback('my_drawing', drawCircle) #connecting callback to a window, or to a function, or connecting them both, or sumn

#SHOW IMAGE WITH OPENCV#

img = np.zeros((512,512,3), np.uint8) #default is uint8 indeed

while True:
    cv2.imshow('my_drawing',img)
    
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()