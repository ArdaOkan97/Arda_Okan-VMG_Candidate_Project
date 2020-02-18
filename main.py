import numpy as np
import cv2
import matplotlib.pyplot as plt
import vmg

videoLoc = 'Set1/4355-4651.avi'

vid = cv2.VideoCapture(videoLoc)

posList = []
height, width, channels = [0,0,0]

while(vid.isOpened()):
    ret, frame = vid.read()
    if not(ret):
        break

    height, width, channels = frame.shape

    # press "q" to exit    
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

    # save detected location of ball
    posList.append(vmg.detectBall(frame))		
    

npPosList = np.array(posList)
xPosList = npPosList[:,0]
yPosList = npPosList[:,1]

vid.release()
cv2.destroyAllWindows()

# plot position of the ball
plt.figure()
plt.plot(xPosList, height-yPosList, 'r+')
plt.xlabel('x (x pixel value)')
plt.ylabel('y (' + str(height) + ' - y pixel value)')
plt.title('ball position for ' + videoLoc)
plt.show(block=True)
