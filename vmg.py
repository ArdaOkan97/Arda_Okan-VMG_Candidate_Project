import numpy as np
import cv2
import imutils

def detectBall(frame):
    # orange range for ball in HSV color space
    orangeLower = (2, 60, 60)
    orangeUpper = (10, 255, 255)

    # add gaussian blur and convert color to HSV
    gausBlur = cv2.GaussianBlur(frame, (11,11), 0)
    hsv = cv2.cvtColor(gausBlur, cv2.COLOR_BGR2HSV)

    # create mask according to color range
    mask = cv2.inRange(hsv, orangeLower, orangeUpper)
    mask = cv2.erode(mask, None, iterations=2)

    # find contour according to the created mask
    contours = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)
    center = None

    # check for found contour
    if len(contours) > 0:
        
	# calculate the center and radius of biggest contour
    	c = max(contours, key=cv2.contourArea)
    	((x, y), radius) = cv2.minEnclosingCircle(c)
    	M = cv2.moments(c)
    	center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
    	
    	# check radius range
    	if (radius > 10) & (radius < 55):
            
    	    # draw the bounding box
    	    cv2.rectangle(frame, (int(x)-int(radius), int(y)-int(radius)),
                (int(x)+int(radius), int(y)+int(radius)),
    	    	(0, 0, 255), 2)

    cv2.imshow('frame (press "q" to quit)',frame)
    #cv2.imshow('mask (press "q" to quit)', mask)
    return center
