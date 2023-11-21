import cv2

# imread() will read the image frame
image = cv2.imread("PRO-104-OpenCV-Image-Assets-main/butterfly.jpg")

greyImage = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

# imshow("name of the application window" , variable in which you have read the image) --> to display the image
cv2.imshow("Butterflyyyy" , greyImage ) 

cv2.waitKey(0)



