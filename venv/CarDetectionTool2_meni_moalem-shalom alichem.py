import cv2
import numpy as np
import time
#from Whatsappmassage import Whatappmassagefunction
#number of constant for calculations
#EmptyParking=1;
FullParking=0;
#Need to intial the parking spots every time reset the code
avialibalrparkingspot=0;#inital number->emptyparking=1=number of all the spots

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
counter3=0;
counter4=0;
bool("Entrparking");
Entrparking=False;#iniatializ
bool("Exitparking");
bool("Leavingparking");
bool("catch_spot_num_1");
bool("catch_spot_num_2");
bool("catch_spot_num_3");
bool("catch_spot_num_4");
bool("catch_spot_num_5");
bool("catch_spot_num_6");
bool("catch_spot_num_7");
bool("catch_spot_num_8");
bool("catch_spot_num_9");

#initiliaz catch const as a function of the spots status
catch_spot_num_1=False;
catch_spot_num_2=True;
catch_spot_num_3=False;
catch_spot_num_4=False;
catch_spot_num_5=True;
catch_spot_num_6=False;
catch_spot_num_7=False;
catch_spot_num_8=True;
catch_spot_num_9=False;

cap = cv2.VideoCapture('meni_moalem_2_day.h264')#VideoCapture(0)-for camera live
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
    if avialibalrparkingspot <= 0:
         avialibalrparkingspot=0
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

        if cv2.contourArea(contour) < 350:#number is the area of the rectangle
            continue
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
        #showing coordinats on screen
        string = str(x) + " " + str(y)
        cv2.putText(frame1, string, (x, y),font, 0.5, (0, 255, 0))

        #cv2.putText(frame1, "Status: {}".format('Movement'), (10, 20), cv2.FONT_HERSHEY_SIMPLEX,
        #            1, (0, 0, 255), 3)
        outallert='Watch-out! Car leaving parking spot!';
        inallert='Watch-out! Car enter parking spot!';

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

        if (x>210 and x<248) and (y>-10 and y<18):
            print(inallert)
            Entrparking=True;
            cv2.putText(frame1, "{}".format('Car/s enter the parking spot!'), (50, 400), cv2.FONT_HERSHEY_SIMPLEX,
                        0.6, (0, 0, 255),1)


        #Spots number 1 Checking
        #if car catch spot num 1
        if (x > 242 and x < 247) and (y > 214 and y < 217) and (catch_spot_num_1==True):
            print(spot1In)
            counterofspot1_in = counterofspot1_in + 1;#counter of changes of frames at spot parking
            if counterofspot1_in > 2:
              avialibalrparkingspot = avialibalrparkingspot - 1;
              catch_spot_num_1 = False
              counterofspot1_in=0
              cv2.putText(frame1, "Status: {}".format('Parking spot num 1 caught'), (10, 100),
                            cv2.FONT_HERSHEY_SIMPLEX,
                             0.6, (0, 0, 255), 1)
        ##if car leaving spot num 1
        if (x > 242 and x < 247) and (y > 214 and y < 217)  and (catch_spot_num_1 == False):
            print(spot1Out)
            counterofspot1_out = counterofspot1_out + 1;  # counter of changes of frames at spot parking
            if counterofspot1_out > 2:
                avialibalrparkingspot = avialibalrparkingspot - 1;
                catch_spot_num_1=True;
                counterofspot1_out=0;
                cv2.putText(frame1, "Status: {}".format('Parking spot num 1 is available to park'), (10, 100),
                                  cv2.FONT_HERSHEY_SIMPLEX,
                                  0.6, (0, 0, 255), 1)

        # Spots number 2 Checking
        # if car catch spot num 2
        if (x > 213 and x < 218) and (y > 146 and y < 151) and (catch_spot_num_2 == True):
            print(spot2In)
            counterofspot2_in = counterofspot2_in + 1;  # counter of changes of frames at spot parking
            if counterofspot2_in > 2:
                avialibalrparkingspot = avialibalrparkingspot - 1;
                catch_spot_num_2 = False
                counterofspot2_in = 0
                cv2.putText(frame1, "Status: {}".format('Parking spot num 2 caught'), (10, 100),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.6, (0, 0, 255), 1)
        ##if car leaving spot num 2
        if (x > 213 and x < 218) and (y > 146 and y < 151) and (catch_spot_num_2 == False):
            print(spot2Out)
            counterofspot2_out = counterofspot2_out + 1;  # counter of changes of frames at spot parking
            if counterofspot2_out > 2:
                avialibalrparkingspot = avialibalrparkingspot - 1;
                counterofspot2_out = 0;
                catch_spot_num_2=True;
                cv2.putText(frame1, "Status: {}".format('Parking spot num 2 is available to park'), (10, 100),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.6, (0, 0, 255), 1)

        # Spots number 3 Checking
        # if car catch spot num 3
        if (x > 192 and x < 197) and (y > 88 and y < 93) and (catch_spot_num_3) == True:
            print(spot3In)
            counterofspot3_in = counterofspot3_in + 1;  # counter of changes of frames at spot parking
            if counterofspot3_in > 2:
                avialibalrparkingspot = avialibalrparkingspot - 1;
                catch_spot_num_3 = False
                counterofspot3_in = 0
                cv2.putText(frame1, "Status: {}".format('Parking spot num 3 caught'), (10, 100),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.6, (0, 0, 255), 1)
        ##if car leaving spot num 3
        if (x > 192 and x < 197) and (y > 88 and y < 93) and catch_spot_num_3 == False:
            print(spot3Out)
            counterofspot3_out = counterofspot3_out + 1;  # counter of changes of frames at spot parking
            if counterofspot3_out > 2:
                avialibalrparkingspot = avialibalrparkingspot - 1;
                counterofspot3_out = 0;
                catch_spot_num_3=True;
                cv2.putText(frame1, "Status: {}".format('Parking spot num 3 is available to park'), (10, 100),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.6, (0, 0, 255), 1)

        # Spots number 4 Checking
        # if car catch spot num 4
        if (x > 188 and x < 193) and (y > 63 and y < 68) and (catch_spot_num_4 == True):
            print(spot4In)
            counterofspot4_in = counterofspot4_in + 1;  # counter of changes of frames at spot parking
            if counterofspot4_in > 2:
                avialibalrparkingspot = avialibalrparkingspot - 1;
                catch_spot_num_4 = False;
                counterofspot4_in = 0
                cv2.putText(frame1, "Status: {}".format('Parking spot num 4 caught!'), (10, 100),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.6, (0, 0, 255), 1)
        ##if car leaving spot num 4
        if (x > 188 and x < 193) and (y > 63 and y < 68)  and (catch_spot_num_4 == False):
            print(spot4Out)
            counterofspot4_out = counterofspot4_out + 1;  # counter of changes of frames at spot parking
            if counterofspot4_out > 2:
                avialibalrparkingspot = avialibalrparkingspot - 1;
                counterofspot4_out = 0;
                catch_spot_num_4=True;
                cv2.putText(frame1, "Status: {}".format('Parking spot num 4 is available to park'), (10, 100),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.6, (0, 0, 255), 1)

        # Spots number 5 Checking
        # if car catch spot num 5
        if (x > 180 and x < 185) and (y > 32 and y < 37) and (catch_spot_num_5 == True):
            print(spot5In)
            counterofspot5_in = counterofspot5_in + 1;  # counter of changes of frames at spot parking
            if counterofspot5_in > 2:
                avialibalrparkingspot = avialibalrparkingspot - 1;
                catch_spot_num_5 = False;
                counterofspot5_in = 0;
                cv2.putText(frame1, "Status: {}".format('Parking spot num 5 caught'), (10, 100),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.6, (0, 0, 255), 1)
        ##if car leaving spot num 5
        if (x > 180 and x < 185) and (y > 32 and y < 37)  and (catch_spot_num_5 == False):
            print(spot5Out)
            counterofspot5_out = counterofspot5_out + 1;  # counter of changes of frames at spot parking
            if counterofspot5_out > 2:
                avialibalrparkingspot = avialibalrparkingspot - 1;
                counterofspot5_out = 0;
                catch_spot_num_5=True;
                cv2.putText(frame1, "Status: {}".format('Parking spot num 5 is available to park'), (10, 100),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.6, (0, 0, 255), 1)

        # Spots number 6 Checking
        # if car catch spot num 6
        if (x > 178 and x < 183) and (y > 7 and y < 12) and (catch_spot_num_6 == True):
            print(spot6In)
            counterofspot6_in = counterofspot6_in + 1;  # counter of changes of frames at spot parking
            if counterofspot6_in > 2:
                avialibalrparkingspot = avialibalrparkingspot - 1;
                catch_spot_num_6 = False;
                counterofspot6_in = 0;
                cv2.putText(frame1, "Status: {}".format('Parking spot num 6 caught!'), (10, 100),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.6, (0, 0, 255), 1)
        ##if car leaving spot num 6
        if (x > 178 and x < 183) and (y > 7 and y < 12) and (catch_spot_num_6 == False):
            print(spot6Out)
            counterofspot6_out = counterofspot6_out + 1;  # counter of changes of frames at spot parking
            if counterofspot6_out > 2:
                avialibalrparkingspot = avialibalrparkingspot - 1;
                counterofspot6_out = 0;
                catch_spot_num_6=True;
                cv2.putText(frame1, "Status: {}".format('Parking spot num 6 is available to park!'), (10, 100),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.6, (0, 0, 255), 1)

        # Spots number 7 Checking
        # if car catch spot num 7
        if (x > 420 and x < 425) and (y > 312 and y < 317) and (catch_spot_num_7 == True):
            print(spot7In)
            counterofspot7_in = counterofspot7_in + 1;  # counter of changes of frames at spot parking
            if counterofspot7_in > 2:
                avialibalrparkingspot = avialibalrparkingspot - 1;
                catch_spot_num_7 = False;
                counterofspot7_in = 0;
                cv2.putText(frame1, "Status: {}".format('Parking spot num 7 caught'), (10, 100),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.6, (0, 0, 255), 1)
        ##if car leaving spot num 7
        if (x > 420 and x < 425) and (y > 312 and y < 317) and (catch_spot_num_7 == False):
            print(spot7Out)
            counterofspot7_out = counterofspot7_out + 1;  # counter of changes of frames at spot parking
            if counterofspot7_out > 2:
                avialibalrparkingspot = avialibalrparkingspot - 1;
                counterofspot7_out = 0;
                catch_spot_num_7=True;
                cv2.putText(frame1, "Status: {}".format('Parking spot num 7 is available to park'), (10, 100),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.6, (0, 0, 255), 1)

        # Spots number 8 Checking
        # if car catch spot num 8
        if (x > 502 and x < 507) and (y > 415 and y <420 ) and (catch_spot_num_8 == True):
            print(spot8In)
            counterofspot8_in = counterofspot8_in + 1;  # counter of changes of frames at spot parking
            if counterofspot8_in > 2:
                avialibalrparkingspot = avialibalrparkingspot - 1;
                catch_spot_num_8 = False;
                counterofspot8_in = 0;
                cv2.putText(frame1, "Status: {}".format('Parking spot num 8 caught!'), (10, 100),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.6, (0, 0, 255), 1)
        ##if car leaving spot num 8
        if (x > 502 and x < 507) and (y > 415 and y <420 )  and (catch_spot_num_8 == False):
            print(spot8Out)
            counterofspot8_out = counterofspot8_out + 1;  # counter of changes of frames at spot parking
            if counterofspot8_out > 2:
                avialibalrparkingspot = avialibalrparkingspot - 1;
                counterofspot8_out = 0;
                catch_spot_num_8=True;
                cv2.putText(frame1, "Status: {}".format('Parking spot num 8 is available to park'), (10, 100),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.6, (0, 0, 255), 1)


        if (x>420 and x<510) and (y>419 and y<479):
            if cv2.contourArea(contour) > 2000:  # number is the area of the rectangle
             print(outallert)
             cv2.putText(frame1, "Status: {}".format('Car/s leaving from parking spot!'), (50, 370), cv2.FONT_HERSHEY_SIMPLEX,
                        0.8, (0, 0, 255), 3)
             Exitparking=True;

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



