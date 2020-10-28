import cv2
import numpy as np

import time
#from Whatsappmassage import Whatappmassagefunction
#number of constant for calculations
#EmptyParking=1;
FullParking=0;
avialibalrparkingspot=1;#inital number->emptyparking=1=number of all the spots
counter1=0;
counterofspot1in=0;
counterofspot1out=0;
counter3=0;
counter4=0;
bool("Entrparking");
Entrparking=False;#iniatializ
bool("Exitparking");

cap = cv2.VideoCapture('Luria11_SapirSagi.h264')#VideoCapture(0)-for camera live
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
        if avialibalrparkingspot <= 0:
            avialibalrparkingspot = 0
        if avialibalrparkingspot == 10:
            cv2.putText(frame1, "Status: {}".format('All parking spots available'),
                        (10, 50), cv2.FONT_HERSHEY_SIMPLEX,
                        0.6, (0, 0, 255), 1)
        if avialibalrparkingspot == FullParking:
            cv2.putText(frame1, "Status: {}".format('All parking spots caught!'),
                        (10, 50), cv2.FONT_HERSHEY_SIMPLEX,
                        0.6, (0, 0, 255), 1)
        if cv2.contourArea(contour) < 200:#number is the area of the rectangle
            continue
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
        #showing coordinats on screen
        string = str(x) + " " + str(y)
        cv2.putText(frame1, string, (x, y),font, 0.9, (0, 255, 0))

        #cv2.putText(frame1, "Status: {}".format('Movement'), (10, 20), cv2.FONT_HERSHEY_SIMPLEX,
        #            1, (0, 0, 255), 3)
        outallert='Watch-out! Car geting out/in parking spot';
        inallert='Watch-out! Car enter/leave the parking spot!';
        spot1Out= 'Allert:"Luria11_SapirSapi street":spot number 1 available'
        spot1In= 'Allert:"Luria11_SapirSapi street": spot number 1 caught'
        if (x>290 and x<325) and (y>90 and y<120):
            print(inallert)
            Entrparking=True;
            cv2.putText(frame1, "{}".format('Car enter the parking spot!'), (10, 80), cv2.FONT_HERSHEY_SIMPLEX,
                        0.6, (0, 0, 255),1)

        #Spots number 1 Checking
        #caught of parking spot number 1
        if (x > 200 and x < 205) and (y > 190 and y < 195) and Entrparking==True:
            print(spot1In)
            counterofspot1in = counterofspot1in + 1;#counter of changes of frames at spot parking
            if counterofspot1in > 2:
              avialibalrparkingspot = avialibalrparkingspot - 1;
              Entrparking == False
              cv2.putText(frame1, "Status: {}".format('Parking spot num 1 caught'), (10, 100),
                            cv2.FONT_HERSHEY_SIMPLEX,
                             0.6, (0, 0, 255), 1)

        #left parking spot number 1
        if (x > 200 and x < 205) and (y > 190 and y < 195) and Entrparking == False:
            print(spot1Out)
            counterofspot1out = counterofspot1out + 1;  # counter of changes of frames at spot parking
            if counterofspot1out > 2:
                avialibalrparkingspot = avialibalrparkingspot - 1;
                counterofspot1out=0
                cv2.putText(frame1, "Status: {}".format('Parking spot num 1 is available'), (10, 100),
                                  cv2.FONT_HERSHEY_SIMPLEX,
                                  0.6, (0, 0, 255), 1)
        #            Whatappmassagefunction(spot1)
#if car going out
        if (x>1 and x<135) and (y>240 and y<395) and cv2.contourArea(contour) > 500:
            print(outallert)
            #counter1=counter1+1;
            if counter1<2:
               # avialibalrparkingspot=avialibalrparkingspot-1;
             cv2.putText(frame1, "Status: {}".format('Car leaving parking spot'), (10, 80), cv2.FONT_HERSHEY_SIMPLEX,
                        1, (0, 0, 255), 3)
             Exitparking=True;
#            Whatappmassagefunction(outallert)


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



