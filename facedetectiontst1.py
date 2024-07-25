import cv2
import numpy as np
import matplotlib.pyplot as plt
font = cv2.FONT_HERSHEY_SIMPLEX
haar_data  = cv2.CascadeClassifier('C:/Users/akash/OneDrive/Documents/data.xml')		
capture = cv2.VideoCapture(0)
while True:
	flag,img = capture.read()
	if flag:
		faces = haar_data.detectMultiScale(img)
		count = len(faces)
		for x,y,w,h in faces:
			cv2.rectangle(img,(x,y),(x+w,y+h),(255,120,255),4)
			
		cv2.putText(img,"No. of faces "+str(count),(0,22),font,0.8,(0,0,0), 2)
		cv2.imshow('result',img)
		
		if(cv2.waitKey(2)==27):
			break;
capture.release()
cv2.destroyAllWindows()