import vmg
import cv2

img = cv2.imread('Results/Test Frame/test.JPG')
print(vmg.detectBall(img))
cv2.waitKey(0)
cv2.destroyAllWindows()
