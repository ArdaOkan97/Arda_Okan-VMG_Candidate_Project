# Arda_Okan-VMG_Candidate_Project
Basketball object detection

Pre-requisites:
- Python 3
- numpy
- matplotlib
- cv2
- imutils

1) Download 'main.py' and 'vmg.py'.
2) Download the videos from Google drive.
3) Set the 'videoLoc' variable in Line 6 of 'main.py' to the location of one of the videos. (i.e. videoLoc = 'Set1/9964-10078.avi')
4) Run 'main.py'. Selected video will run and the ball will be detected by the program and enclosed with a red square.
   After the video runs, the x-y coordinates of the detected ball will be displayed in a figure.

More information about the algorithm can be seen in the report.

You can run 'test.py' after downloading all files in this project to see how 'detectBall()' function works in 'vmg.py'.
Uncomment Line 42 in 'vmg.py' to see the generated mask for each frame. 
