import cv2
import numpy as np

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import time
from Whatsappmassage import Whatappmassagefunction
#number of constant for calculations
#EmptyParking=1;
FullParking=0;
avialibalrparkingspot=1;#inital number->emptyparking=1=number of all the spots
counter1=0;
counterofspot1=0;
counter3=0;
counter4=0;
bool("Entrparking");
bool("Exitparking");

cap = cv2.VideoCapture('carsparking12_c.mp4')#VideoCapture(0)-for camera live
frame_width = int( cap.get(cv2.CAP_PROP_FRAME_WIDTH))

frame_height =int( cap.get( cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc('X','V','I','D')

out = cv2.VideoWriter("output.avi", fourcc, 5.0, (1280,720))#record the output and send it to some path

font = cv2.FONT_HERSHEY_COMPLEX
ret, frame1 = cap.read()
ret, frame2 = cap.read()
print(frame1.shape)

while cap.isOpened():
    diff = cv2.absdiff(frame1, frame2)
    image1=out.write(diff)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.putText(frame1, "{}".format('Num of available parking spots:'+ str(avialibalrparkingspot)+''), (10, 20), cv2.FONT_HERSHEY_SIMPLEX,
                0.6, (0, 0, 255), 1)
    if avialibalrparkingspot==10:
        cv2.putText(frame1, "Status: {}".format('All parking spots available' ),
                    (10, 50), cv2.FONT_HERSHEY_SIMPLEX,
                    0.6, (0, 0, 255), 1)
    if  avialibalrparkingspot==FullParking:
        cv2.putText(frame1, "Status: {}".format('All parking spots caught!'),
                    (10, 50), cv2.FONT_HERSHEY_SIMPLEX,
                    0.6, (0, 0, 255), 1)
    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)
        print('Number of available parking spot:'+ str(avialibalrparkingspot)+'')

        if cv2.contourArea(contour) < 500:#number is the area of the rectangle
            continue
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
        #showing coordinats on screen
        string = str(x) + " " + str(y)
        cv2.putText(frame1, string, (x, y),font, 0.5, (0, 255, 0))

        #cv2.putText(frame1, "Status: {}".format('Movement'), (10, 20), cv2.FONT_HERSHEY_SIMPLEX,
        #            1, (0, 0, 255), 3)
        MotionAllert='Car Movement Please contact the hunter/check sensor for the specific parking street';
        outallert='Watch-out! Car geting out parking spot';
        inallert='Watch-out! Car enter the parking spot!';
        spot1='Allert:"Hovevi Chion street": parking Spots number 1 caught'
        if (x>0 and x<50) and (y>154 and y<471):
            print(inallert)
            Entrparking=True;
            cv2.putText(frame1, "{}".format('Car enter the parking spot!'), (10, 80), cv2.FONT_HERSHEY_SIMPLEX,
                        0.6, (0, 0, 255),1)
            #counter2 = counter2 + 1;
        #if counter2 < 2:
                #avialibalrparkingspot = avialibalrparkingspot + 1;
        if (x > 200 and x < 250) and (y > 160 and y < 195) and Entrparking==True:
            print(spot1)
            counterofspot1 = counterofspot1 + 1;
            if counterofspot1 < 2:
              avialibalrparkingspot = avialibalrparkingspot - 1;
              cv2.putText(frame1, "Status: {}".format('Parking spot num 1 caught'), (10, 100),
                            cv2.FONT_HERSHEY_SIMPLEX,
                             0.6, (0, 0, 255), 1)
            #Whatappmassagefunction(spot1)

        if (x>500 and x<600) and (y>400 and y<500):
            print(outallert)
            counter1=counter1+1;
            if counter1<2:
               # avialibalrparkingspot=avialibalrparkingspot-1;
             cv2.putText(frame1, "Status: {}".format('Car going out from parking spot'), (10, 80), cv2.FONT_HERSHEY_SIMPLEX,
                        1, (0, 0, 255), 3)
             Exitparking=True;
#            Whatappmassagefunction(outallert)

        #Whatappmassagefunction(allert);
    #cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)

    image = cv2.resize(frame1, (1280,720))
    out.write(image)
    cv2.imshow("feed", frame1)

    frame1 = frame2
    ret, frame2 = cap.read()

    # channels = cv2.mean(frame2)
    # observation = np.array([(channels[2], channels[1], channels[0])])
    # if np.mean(observation)<130 and np.mean(observation)>120:#128 value is gray in RGB
    #     print("Gray image/Empty parking")

    # _, binaryimage = cv2.threshold( frame2, 209, 255, cv2.THRESH_BINARY)
    # print(binaryimage)

    if cv2.waitKey(40) == 27:
        break

cv2.destroyAllWindows()
cap.release()
out.release()



