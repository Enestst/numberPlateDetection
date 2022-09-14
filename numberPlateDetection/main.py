import cv2 as cv

# properties of the camera
frameWidth = 640 
frameHeight = 480

cap = cv.VideoCapture(0) # 0 is the default camera
cap.set(3, frameWidth)
cap.set(4, frameHeight) 
cap.set(10, 100) 



cascade = cv.CascadeClassifier("resources/haarcascade_russian_plate_number.xml") # load the cascade classifier 


cnt = 0
# main loop
while True:
    suc, img = cap.read() # read the image
    imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) # convert to grayscale
    numberPlates = cascade.detectMultiScale(imgGray, 1.1, 4) # detect the number plates
    for (x, y, width, height) in numberPlates:# draw a rectangle around the number plates
        if width*height  > 150:# only draw the rectangle if the area is greater than 150
            cv.rectangle(img, (x, y), (x+width, y+height), (0, 255, 0), 2)
            cv.putText(img, "NUMBER PLATE", (x, y-10), cv.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 255, 0), 2)
            imgRoi = img[y:y+height, x:x+width] # crop the number plate
            cv.imshow("ROI", imgRoi) # show the cropped number plate
    cv.imshow("Result", img) # show the image
    if cv.waitKey(1) & 0xFF == ord('q'):
        cv.imwrite("Resources/Scanned/NoPlate_"+str(cnt)+".jpg",imgRoi) # save the cropped number plate
        cv.rectangle(img,(0,200),(640,300),(0,255,0),cv.FILLED)# draw a rectangle to show the user that the number plate has been saved
        cv.putText(img,"Scan Saved",(150,265),cv.FONT_HERSHEY_DUPLEX,2,(0,0,255),2) # show the user that the number plate has been saved
        cv.imshow("Result",img)
        cv.waitKey(500)
        cnt += 1
        
