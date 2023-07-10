import cv2

img = cv2.imread("viru.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
invert = cv2.bitwise_not(gray)
blur = cv2.GaussianBlur(invert, (21, 21), 0)
invertblu = cv2.bitwise_not(blur)
sketch = cv2.divide(gray, invertblu, scale=256.0)
cv2.imshow("original image", sketch)

cv2.waitKey(0)
