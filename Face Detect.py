import cv2
img=cv2.imread('1.jpg')
grayi=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
haar_cascade_faces=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
face_rect=haar_cascade_faces.detectMultiScale(grayi,scaleFactor=1.2,minNeighbors=5)
for x,y,w,h in face_rect:
 cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
cv2.imshow('my  face',img)
cv2.waitKey(0)
cv2.destroyAllWindows()