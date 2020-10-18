import cv2
import numpy as np

import time
#from Whatsappmassage import Whatappmassagefunction
from EmailAleert import MailAllertFunc
#number of constant for calculations
#EmptyParking=1;
FullParking=0;
avialibalrparkingspot=2;#inital number->emptyparking=1=number of all the spots
counter_of_frames_leaving_park=0;
counterof_frames_spot1_in=0;
counterof_frames_spot1_out=0;
counterof_frames_spot2 = 0
bool("Entrparking");
Entrparking=False;#iniatializ
bool("Exitparking");

cap = cv2.VideoCapture('kern-shalom-alichem-day6.mov')#VideoCapture(0)-for camera live
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
                0.7, (0, 0, 255), 1)
    if avialibalrparkingspot <= 0:
         avialibalrparkingspot=0
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
        cv2.putText(frame1, string, (x, y),font, 0.7, (0, 255, 0))

        #cv2.putText(frame1, "Status: {}".format('Movement'), (10, 20), cv2.FONT_HERSHEY_SIMPLEX,
        #            1, (0, 0, 255), 3)
        outallert='Watch-out! Car going out the parking spot!';
        inallert='Watch-out! Car enter the parking spot!';
        spot1Out= 'Allert:"Hovevi Chion street":Car going out, parking Spots number 1 available'
        spot1In= 'Allert:"Hovevi Chion street": parking Spots number 1 caught'
        spot2Out = 'Allert:"Hovevi Chion street":Car going out, parking Spots number 2 available'
        spot2In = 'Allert:"Hovevi Chion street": parking Spots number 2 caught'
        if (x>40 and x<70) and (y>60 and y<80):
            print(inallert)
            Entrparking=True;
            cv2.putText(frame1, "{}".format('Car enter the parking spot!'), (50, 400), cv2.FONT_HERSHEY_SIMPLEX,
                        0.7, (0, 0, 255),3)

        #Spots number 1 Checking
        # if car enter the parking
        if (x > 64 and x < 66) and (y >80  and y < 88) and Entrparking==True:
            print(spot1In)
            counterof_frames_spot1_in=0
            counterof_frames_spot1_in = counterof_frames_spot1_in + 1;#counter of changes of frames at spot parking
            if counterof_frames_spot1_in < 2:
              avialibalrparkingspot = avialibalrparkingspot - 1;
              cv2.putText(frame1, "Status: {}".format('Parking spot num 1 caught'), (10, 100),
                            cv2.FONT_HERSHEY_SIMPLEX,
                             0.7, (0, 0, 255), 1)
#            Whatappmassagefunction(spot1)
           # MailAllertFunc(spot1In)
        #if car leaving the parking spot
        if (x > 90 and x < 94) and (y >105 and y < 107) :
            print(spot1Out)
            #counterof_frames_spot1=0
            counterof_frames_spot1_out = counterof_frames_spot1_out + 1;  # counter of changes of frames at spot parking
            if counterof_frames_spot1_out < 2:
                avialibalrparkingspot = avialibalrparkingspot + 1;
                cv2.putText(frame1, "Status: {}".format('Parking spot num 1 is free to park'), (10, 100),
                                  cv2.FONT_HERSHEY_SIMPLEX,
                                  0.7, (0, 0, 255), 1)
        #            Whatappmassagefunction(spot1)
                #MailAllertFunc(spot1Out)

                # Spots number 2 Checking
                # if car enter the parking
        if (x > 61 and x < 73) and (y > 70 and y < 73) and Entrparking == True:
            print(spot2In)
            counterof_frames_spot2 = counterof_frames_spot2 + 1;  # counter of changes of frames at spot parking
            if counterof_frames_spot2 < 2:
                avialibalrparkingspot = avialibalrparkingspot - 1;
                cv2.putText(frame1, "Status: {}".format('Parking spot num 2 caught!'), (10, 100),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.7, (0, 0, 255), 1)
                #            Whatappmassagefunction(spot1)
                # MailAllertFunc(spot1In)
        # if car going out the parking
        if (x > 61 and x < 69) and (y > 70 and y < 73) and Entrparking == False:
            print(spot2Out)
            # counterof_frames_spot2=0
            counterof_frames_spot2 = counterof_frames_spot2 + 1;  # counter of changes of frames at spot parking
            if counterof_frames_spot2 < 2:
                    avialibalrparkingspot = avialibalrparkingspot + 1;
                    cv2.putText(frame1, "Status: {}".format('Parking spot num 2 is free to park'), (10, 100),
                                    cv2.FONT_HERSHEY_SIMPLEX,
                                    0.7, (0, 0, 255), 1)
                #            Whatappmassagefunction(spot1)
                # MailAllertFunc(spot1Out)

                # if car leaving the parking
        if (x>420 and x<641) and (y>370 and y<480):
            print(outallert)
            cv2.putText(frame1, "Status: {}".format('Car going out from parking spot'), (50, 400), cv2.FONT_HERSHEY_SIMPLEX,
                        0.8, (0, 0, 255), 3)
            Exitparking=True;
#           Whatappmassagefunction(outallert)

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



