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
counterofspot1_in=0;
counterofspot1_out=0;
counterofspot2_in=0;
counterofspot2_out=0;
counterofspot3_in=0;
counterofspot3_out=0;
counterofspot4_in=0;
counterofspot4_out=0;
counterofspot5_in=0;
counterofspot5_out=0;
counterofspot6_in=0;
counterofspot6_out=0;
counterofspot7_in=0;
counterofspot7_out=0;
counterofspot8_in=0;
counterofspot8_out=0;
counter4=0;
bool("Entrparking");
Entrparking=False;#iniatializ
bool("Exitparking");

cap = cv2.VideoCapture('srkin21_yarden_adom_day.h264')#VideoCapture(0)-for camera live
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
        outallert='Watch-out! Car/s leaving parking lot';
        inallert='Watch-out! Car/s enter the parking lot!';

        spot1Out= 'Allert:"Sirkin 21 street": parking Spot number 1 available!'
        spot1In= 'Allert:"Sirkin 21 street": parking Spot number 1 caught!'
        spot2Out= 'Allert:"Sirkin 21 street": parking Spot number 2 available!'
        spot2In= 'Allert:"Sirkin 21 street": parking Spot number 2 caught!'
        spot3Out= 'Allert:"Sirkin 21 street": parking Spot number 3 available!'
        spot3In= 'Allert:"Sirkin 21 street": parking Spot number 3 caught!'
        spot4Out= 'Allert:"Sirkin 21 street": parking Spot number 4 available!'
        spot4In= 'Allert:"Sirkin 21 street": parking Spot number 4 caught!'
        spot5Out= 'Allert:"Sirkin 21 street": parking Spot number 5 available!'
        spot5In= 'Allert:"Sirkin 21 street": parking Spot number 5 caught!'
        spot6Out= 'Allert:"Sirkin 21 street": parking Spot number 6 available!'
        spot6In= 'Allert:"Sirkin 21 street": parking Spot number 6 caught!'
        spot7Out= 'Allert:"Sirkin 21 street": parking Spot number 7 available!'
        spot7In= 'Allert:"Sirkin 21street": parking Spot number 7 caught!'
        spot8Out= 'Allert:"Sirkin 21 street": parking Spot number 8 available!'
        spot8In= 'Allert:"Sirkin 21 street": parking Spot number 8 caught!'
        spot9Out= 'Allert:"Sirkin 21 street": parking Spot number 9 available!'
        spot9In= 'Allert:"Sirkin 21 street": parking Spot number 9 caught!'
        #car enter to park checking
        if (x>40 and x<100) and (y>80 and y<105):
            print(inallert)
            Entrparking=True;
            cv2.putText(frame1, "{}".format('Car/s enter the parking spot!'), (50, 400), cv2.FONT_HERSHEY_SIMPLEX,
                        0.6, (0, 0, 255),1)

        #Spots number 1 Checking
        #if car catch spot num 1
        if (x > 284 and x < 289) and (y > 393 and y < 398) and Entrparking==True:
            print(spot1In)
            counterofspot1_in = counterofspot1_in + 1;#counter of changes of frames at spot parking
            if counterofspot1_in < 2:
              avialibalrparkingspot = avialibalrparkingspot - 1;
              Entrparking = False
              counterofspot1_in=0
              cv2.putText(frame1, "Status: {}".format('Parking spot num 1 caught'), (10, 100),
                            cv2.FONT_HERSHEY_SIMPLEX,
                             0.6, (0, 0, 255), 1)
        ##if car leaving spot num 1
        if (x > 284 and x < 289) and (y > 393 and y < 398)  and Entrparking == False:
            print(spot1Out)
            counterofspot1_out = counterofspot1_out + 1;  # counter of changes of frames at spot parking
            if counterofspot1_out < 2:
                avialibalrparkingspot = avialibalrparkingspot - 1;
                counterofspot1_out=0;
                cv2.putText(frame1, "Status: {}".format('Parking spot num 1 is available to park'), (10, 100),
                                  cv2.FONT_HERSHEY_SIMPLEX,
                                  0.6, (0, 0, 255), 1)
        # Spots number 2 Checking
        # if car catch spot num 2
        if (x > 200 and x < 225) and (y > 160 and y < 195) and Entrparking == True:
            print(spot2In)
            counterofspot2_in = counterofspot2_in + 1;  # counter of changes of frames at spot parking
            if counterofspot2_in < 2:
                avialibalrparkingspot = avialibalrparkingspot - 1;
                Entrparking = False
                counterofspot2_in = 0
                cv2.putText(frame1, "Status: {}".format('Parking spot num 2 caught'), (10, 100),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.6, (0, 0, 255), 1)
        ##if car leaving spot num 2
        if (x > 200 and x < 225) and (y > 160 and y < 195) and Entrparking == False:
            print(spot2Out)
            counterofspot2_out = counterofspot2_out + 1;  # counter of changes of frames at spot parking
            if counterofspot2_out < 2:
                avialibalrparkingspot = avialibalrparkingspot - 1;
                counterofspot2_out = 0;
                cv2.putText(frame1, "Status: {}".format('Parking spot num 2 is available to park'), (10, 100),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.6, (0, 0, 255), 1)
        # Spots number 3 Checking
        # if car catch spot num 3
        if (x > 342 and x < 347) and (y > 266 and y < 271) and Entrparking == True:
            print(spot3In)
            counterofspot3_in = counterofspot3_in + 1;  # counter of changes of frames at spot parking
            if counterofspot3_in < 2:
                avialibalrparkingspot = avialibalrparkingspot - 1;
                Entrparking = False
                counterofspot3_in = 0
                cv2.putText(frame1, "Status: {}".format('Parking spot num 3 caught'), (10, 100),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.6, (0, 0, 255), 1)
        ##if car leaving spot num 3
        if (x > 342 and x < 347) and (y > 266 and y < 271) and Entrparking == False:
            print(spot3Out)
            counterofspot3_out = counterofspot3_out + 1;  # counter of changes of frames at spot parking
            if counterofspot3_out < 2:
                avialibalrparkingspot = avialibalrparkingspot - 1;
                counterofspot3_out = 0;
                cv2.putText(frame1, "Status: {}".format('Parking spot num 3 is available to park'), (10, 100),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.6, (0, 0, 255), 1)
        # Spots number 4 Checking
        # if car catch spot num 4
        if (x > 362 and x < 367) and (y > 221 and y < 226) and Entrparking == True:
            print(spot4In)
            counterofspot4_in = counterofspot4_in + 1;  # counter of changes of frames at spot parking
            if counterofspot4_in < 2:
                avialibalrparkingspot = avialibalrparkingspot - 1;
                Entrparking = False
                counterofspot4_in = 0
                cv2.putText(frame1, "Status: {}".format('Parking spot num 4 caught!'), (10, 100),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.6, (0, 0, 255), 1)
        ##if car leaving spot num 4
        if (x > 362 and x < 367) and (y > 221 and y < 226)  and Entrparking == False:
            print(spot4Out)
            counterofspot4_out = counterofspot4_out + 1;  # counter of changes of frames at spot parking
            if counterofspot4_out < 2:
                avialibalrparkingspot = avialibalrparkingspot - 1;
                counterofspot4_out = 0;
                cv2.putText(frame1, "Status: {}".format('Parking spot num 4 is available to park'), (10, 100),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.6, (0, 0, 255), 1)
        # Spots number 5 Checking
        # if car catch spot num 5
        if (x > 114 and x < 119) and (y > 405 and y < 410) and Entrparking == True:
            print(spot5In)
            counterofspot5_in = counterofspot5_in + 1;  # counter of changes of frames at spot parking
            if counterofspot5_in < 2:
                avialibalrparkingspot = avialibalrparkingspot - 1;
                Entrparking = False
                counterofspot5_in = 0
                cv2.putText(frame1, "Status: {}".format('Parking spot num 5 caught'), (10, 100),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.6, (0, 0, 255), 1)
        ##if car leaving spot num 5
        if (x > 114 and x < 119) and (y > 405 and y < 410) and Entrparking == False:
            print(spot5Out)
            counterofspot5_out = counterofspot5_out + 1;  # counter of changes of frames at spot parking
            if counterofspot5_out < 2:
                avialibalrparkingspot = avialibalrparkingspot - 1;
                counterofspot5_out = 0;
                cv2.putText(frame1, "Status: {}".format('Parking spot num 5 is available to park'), (10, 100),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.6, (0, 0, 255), 1)
        # Spots number 6 Checking
        # if car catch spot num 6
        if (x > 174 and x < 179) and (y > 336 and y < 341) and Entrparking == True:
            print(spot6In)
            counterofspot6_in = counterofspot6_in + 1;  # counter of changes of frames at spot parking
            if counterofspot6_in < 2:
                avialibalrparkingspot = avialibalrparkingspot - 1;
                Entrparking = False
                counterofspot6_in = 0
                cv2.putText(frame1, "Status: {}".format('Parking spot num 6 caught!'), (10, 100),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.6, (0, 0, 255), 1)
        ##if car leaving spot num 6
        if (x > 174 and x < 179) and (y > 336 and y < 341) and Entrparking == False:
            print(spot6Out)
            counterofspot6_out = counterofspot6_out + 1;  # counter of changes of frames at spot parking
            if counterofspot6_out < 2:
                avialibalrparkingspot = avialibalrparkingspot - 1;
                counterofspot6_out = 0;
                cv2.putText(frame1, "Status: {}".format('Parking spot num 6 is available to park!'), (10, 100),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.6, (0, 0, 255), 1)
        # Spots number 7 Checking
        # if car catch spot num 7
        if (x > 263 and x < 268) and (y > 248 and y < 253) and Entrparking == True:
            print(spot7In)
            counterofspot7_in = counterofspot7_in + 1;  # counter of changes of frames at spot parking
            if counterofspot7_in < 2:
                avialibalrparkingspot = avialibalrparkingspot - 1;
                Entrparking = False
                counterofspot7_in = 0
                cv2.putText(frame1, "Status: {}".format('Parking spot num 7 caught'), (10, 100),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.6, (0, 0, 255), 1)
        ##if car leaving spot num 7
        if (x > 263 and x < 268) and (y > 248 and y < 253) and Entrparking == False:
            print(spot7Out)
            counterofspot7_out = counterofspot7_out + 1;  # counter of changes of frames at spot parking
            if counterofspot7_out < 2:
                avialibalrparkingspot = avialibalrparkingspot - 1;
                counterofspot7_out = 0;
                cv2.putText(frame1, "Status: {}".format('Parking spot num 7 is available to park'), (10, 100),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.6, (0, 0, 255), 1)
        # Spots number 8 Checking
        # if car catch spot num 8
        if (x > 200 and x < 225) and (y > 160 and y < 195) and Entrparking == True:
            print(spot1In)
            counterofspot1_in = counterofspot1_in + 1;  # counter of changes of frames at spot parking
            if counterofspot1_in < 2:
                avialibalrparkingspot = avialibalrparkingspot - 1;
                Entrparking = False
                counterofspot1_in = 0
                cv2.putText(frame1, "Status: {}".format('Parking spot num 1 caught'), (10, 100),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.6, (0, 0, 255), 1)
        ##if car leaving spot num 1
        if (x > 200 and x < 225) and (y > 160 and y < 195) and Entrparking == False:
            print(spot1Out)
            counterofspot1_out = counterofspot1_out + 1;  # counter of changes of frames at spot parking
            if counterofspot1_out < 2:
                avialibalrparkingspot = avialibalrparkingspot - 1;
                counterofspot1_out = 0;
                cv2.putText(frame1, "Status: {}".format('Parking spot num 1 is available to park'), (10, 100),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.6, (0, 0, 255), 1)

        if (x > 200 and x < 225) and (y > 160 and y < 195) and Entrparking == True:
            print(spot1In)
            counterofspot1_in = counterofspot1_in + 1;  # counter of changes of frames at spot parking
            if counterofspot1_in < 2:
                avialibalrparkingspot = avialibalrparkingspot - 1;
                Entrparking = False
                counterofspot1_in = 0
                cv2.putText(frame1, "Status: {}".format('Parking spot num 1 caught'), (10, 100),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.6, (0, 0, 255), 1)
        ##if car leaving spot num 1
        if (x > 200 and x < 225) and (y > 160 and y < 195) and Entrparking == False:
            print(spot1Out)
            counterofspot1_out = counterofspot1_out + 1;  # counter of changes of frames at spot parking
            if counterofspot1_out < 2:
                avialibalrparkingspot = avialibalrparkingspot - 1;
                counterofspot1_out = 0;
                cv2.putText(frame1, "Status: {}".format('Parking spot num 1 is available to park'), (10, 100),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.6, (0, 0, 255), 1)

        if (x > 200 and x < 225) and (y > 160 and y < 195) and Entrparking == True:
            print(spot1In)
            counterofspot1_in = counterofspot1_in + 1;  # counter of changes of frames at spot parking
            if counterofspot1_in < 2:
                avialibalrparkingspot = avialibalrparkingspot - 1;
                Entrparking = False
                counterofspot1_in = 0
                cv2.putText(frame1, "Status: {}".format('Parking spot num 1 caught'), (10, 100),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.6, (0, 0, 255), 1)
        ##if car leaving spot num 1
        if (x > 200 and x < 225) and (y > 160 and y < 195) and Entrparking == False:
            print(spot1Out)
            counterofspot1_out = counterofspot1_out + 1;  # counter of changes of frames at spot parking
            if counterofspot1_out < 2:
                avialibalrparkingspot = avialibalrparkingspot - 1;
                counterofspot1_out = 0;
                cv2.putText(frame1, "Status: {}".format('Parking spot num 1 is free to park'), (10, 100),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.6, (0, 0, 255), 1)

        if (x > 200 and x < 225) and (y > 160 and y < 195) and Entrparking == True:
            print(spot1In)
            counterofspot1_in = counterofspot1_in + 1;  # counter of changes of frames at spot parking
            if counterofspot1_in < 2:
                avialibalrparkingspot = avialibalrparkingspot - 1;
                Entrparking = False
                counterofspot1_in = 0
                cv2.putText(frame1, "Status: {}".format('Parking spot num 1 caught'), (10, 100),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.6, (0, 0, 255), 1)
        ##if car leaving spot num 1
        if (x > 200 and x < 225) and (y > 160 and y < 195) and Entrparking == False:
            print(spot1Out)
            counterofspot1_out = counterofspot1_out + 1;  # counter of changes of frames at spot parking
            if counterofspot1_out < 2:
                avialibalrparkingspot = avialibalrparkingspot - 1;
                counterofspot1_out = 0;
                cv2.putText(frame1, "Status: {}".format('Parking spot num 1 is free to park'), (10, 100),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.6, (0, 0, 255), 1)
        #

        if (x>450 and x<500) and (y>310 and y<330):
            print(outallert)
            counter1=counter1+1;
            if counter1<2:
               # avialibalrparkingspot=avialibalrparkingspot-1;
             cv2.putText(frame1, "Status: {}".format('Car leaving parking spot'), (50, 370), cv2.FONT_HERSHEY_SIMPLEX,
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



