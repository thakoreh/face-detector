import cv2

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img=cv2.imread("hiren.jpg")
resized_img=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))

gray_img=cv2.cvtColor(resized_img,cv2.COLOR_BGR2GRAY)

faces=face_cascade.detectMultiScale(gray_img,
scaleFactor=1.1,
minNeighbors=5)

for x,y,w,h in faces:
    img=cv2.rectangle(resized_img,(x,y),(x+w,y+h),(0,255,0),3)



print(faces)

cv2.imshow("Gray",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
