import cv2
import numpy as np

import time
#from Whatsappmassage import Whatappmassagefunction
#from EmailAleert import MailAllertFunc
#number of constant for calculations
#EmptyParking=1;
FullParking=0;
avialibalrparkingspot=1;#inital number->emptyparking=1=number of all the spots
counter_of_frames_leaving_park=0;
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
bool("Entrparking");
Entrparking=False;#iniatializ
bool("Leavingparking");
bool("catch_spot_num_1");
bool("catch_spot_num_2");
bool("catch_spot_num_3");
bool("catch_spot_num_4");
bool("catch_spot_num_5");
bool("spot_num_1_ready_out");
bool("spot_num_1_ready_in");

#initiliaz catch const as a function of the spots status
#False=>spot caught
#True=>Spot free
catch_spot_num_1=False;
catch_spot_num_2=False;
catch_spot_num_3=False;
catch_spot_num_4=False;
catch_spot_num_5=False;
spot_num_1_ready_out=False;
spot_num_1_ready_in=False;
Leavingparking=False;
cap = cv2.VideoCapture('shalom-alichem-keren-shalom-day-23-10-20_a.avi')#VideoCapture(0)-for camera live
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
                0.7, (0, 0, 255), 2)
    if avialibalrparkingspot <= 0:
         avialibalrparkingspot=0
    if avialibalrparkingspot==10:
        cv2.putText(frame1, "Status: {}".format('All parking spots available' ),
                    (10, 50), cv2.FONT_HERSHEY_SIMPLEX,
                    0.6, (0, 0, 255), 2)
    if  avialibalrparkingspot==FullParking:
        cv2.putText(frame1, "Status: {}".format('All parking spots caught!'),
                    (10, 50), cv2.FONT_HERSHEY_SIMPLEX,
                    0.6, (0, 0, 255), 2)
    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)
        print('Number of available parking spot:'+ str(avialibalrparkingspot)+'')

        if cv2.contourArea(contour) < 520:#The number is the area of the rectangle
            continue
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
        #showing coordinats on screen
        string = str(x) + " " + str(y)
        cv2.putText(frame1, string, (x, y),font, 0.7, (0, 255, 0))

        outallert='Watch-out! Car going out the parking spot!';
        inallert='Watch-out! Car enter the parking spot!';
        spot1Out= 'Allert:"Hovevi Chion street":Car going out, parking Spots number 1 available'
        spot1In= 'Allert:"Hovevi Chion street": parking Spots number 1 caught'
        spot2Out = 'Allert:"Hovevi Chion street":Car going out, parking Spots number 2 available'
        spot2In = 'Allert:"Hovevi Chion street": parking Spots number 2 caught'
        spot3Out = 'Allert:"Hovevi Chion street":Car going out, parking Spots number 3 available'
        spot3In = 'Allert:"Hovevi Chion street": parking Spots number 3 caught!'
        spot4Out = 'Allert:"Hovevi Chion street":Car going out, parking Spots number 4 available'
        spot4In = 'Allert:"Hovevi Chion street": parking Spots number 4 caught!'
        spot5Out = 'Allert:"Hovevi Chion street":Car going out, parking Spots number 5 available'
        spot5In = 'Allert:"Hovevi Chion street": parking Spots number 5 caught!'
        if (x>40 and x<78) and (y>51 and y<72):
            print(inallert)
            Entrparking=True;
            cv2.putText(frame1, "{}".format('Car/s enter the parking spot!'), (50, 400), cv2.FONT_HERSHEY_SIMPLEX,
                        0.9, (0, 0, 255),3)

            # Spots number 1 Checking
            # if car catch spot num 1
            #option 1-front
        if (x > 470 and x < 475) and (y > 447 and y < 452) and (catch_spot_num_1 == True):
            print(spot1In)
            counterofspot1_in = counterofspot1_in + 1;  # counter of changes of frames at spot parking
            if counterofspot1_in > 4:
                avialibalrparkingspot = avialibalrparkingspot - 1;
                catch_spot_num_1 = False;
                counterofspot1_in = 0;
                cv2.putText(frame1, "Status: {}".format('Parking spot num 1 caught'), (10, 100),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.6, (0, 0, 255), 1)

            #option 2-reverse
            ##if car going to catch spot num 1 by reverse
        if (x > 554 and x <559 ) and (y > 447 and y < 452) and (catch_spot_num_1 == True):
            print("car going to catch spot number 1 by reverse,ready==True")
            spot_num_1_ready_in=True;

        if (x > 520 and x < 558) and (y > 442 and y < 452) and (catch_spot_num_1 == True) and (spot_num_1_ready_in==True):
            print(spot1In)
            counterofspot1_in = counterofspot1_in + 1;  # counter of changes of frames at spot parking
            if counterofspot1_in > 2:
                avialibalrparkingspot = avialibalrparkingspot - 1;
                catch_spot_num_1 = False;
                counterofspot1_in = 0;
                cv2.putText(frame1, "Status: {}".format('Parking spot num 1 caught'), (10, 100),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.6, (0, 0, 255), 1)



            ##if car going to leave spot num 1
        if (x > 534 and x < 567) and (y > 437 and y < 459) and (catch_spot_num_1 == False):
            print("car going to leave spot number 1,ready==True")
            spot_num_1_ready_out=True;

            ##if car leaving spot num 1
        if (x > 520 and x < 570 ) and (y > 435 and y < 460) and (catch_spot_num_1 == False) and ( spot_num_1_ready_out==True):
            print(spot1Out)
            counterofspot1_out = counterofspot1_out + 1;  # counter of changes of frames at spot parking
            if counterofspot1_out > 2:
                avialibalrparkingspot = avialibalrparkingspot + 1;
                counterofspot1_out = 0;
                catch_spot_num_1 = True;
                cv2.putText(frame1, "Status: {}".format('Parking spot num 1 is available to park'), (10, 100),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.6, (0, 0, 255), 1)


            # Spots number 2 Checking
            # if car catch spot num 2
        if (x > 336 and x < 341) and (y > 328 and y < 333) and (catch_spot_num_2 == True):
            print(spot2In)
            counterofspot2_in = counterofspot2_in + 1;  # counter of changes of frames at spot parking
            if counterofspot2_in > 2:
                avialibalrparkingspot = avialibalrparkingspot - 1;
                catch_spot_num_2 = False;
                counterofspot2_in = 0;
                cv2.putText(frame1, "Status: {}".format('Parking spot num 2 caught'), (10, 100),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.6, (0, 0, 255), 1)
            ##if car leaving spot num 2
        if (x > 336 and x < 341) and (y > 328 and y < 333) and (catch_spot_num_2 == False):
            print(spot2Out)
            counterofspot2_out = counterofspot2_out + 1;  # counter of changes of frames at spot parking
            if counterofspot2_out > 2:
                avialibalrparkingspot = avialibalrparkingspot - 1;
                counterofspot2_out = 0;
                catch_spot_num_2 = True;
                cv2.putText(frame1, "Status: {}".format('Parking spot num 2 is available to park'), (10, 100),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.6, (0, 0, 255), 1)

            # Spots number 3 Checking
            # if car catch spot num 3
        if (x > 213 and x < 218) and (y > 228 and y < 233) and (catch_spot_num_3 == True):
            print(spot3In)
            counterofspot3_in = counterofspot3_in + 1;  # counter of changes of frames at spot parking
            if counterofspot3_in > 2:
                avialibalrparkingspot = avialibalrparkingspot - 1;
                catch_spot_num_3 = False;
                counterofspot3_in = 0
                cv2.putText(frame1, "Status: {}".format('Parking spot num 3 caught'), (10, 100),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.6, (0, 0, 255), 1)
            ##if car leaving spot num 3
        if (x > 213 and x < 218) and (y > 228 and y < 233) and (catch_spot_num_3 == False):
            print(spot3Out)
            counterofspot3_out = counterofspot3_out + 1;  # counter of changes of frames at spot parking
            if counterofspot3_out > 2:
                avialibalrparkingspot = avialibalrparkingspot - 1;
                counterofspot3_out = 0;
                catch_spot_num_3 = True;
                cv2.putText(frame1, "Status: {}".format('Parking spot num 3 is available to park'), (10, 100),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.6, (0, 0, 255), 1)

            # Spots number 4 Checking
            # if car catch spot num 4
        if (x > 156 and x < 161) and (y > 185 and y < 190) and (catch_spot_num_4 == True):
            print(spot4In)
            counterofspot4_in = counterofspot4_in + 1;  # counter of changes of frames at spot parking
            if counterofspot4_in > 2:
                avialibalrparkingspot = avialibalrparkingspot - 1;
                catch_spot_num_4 = False;
                counterofspot4_in = 0;
                cv2.putText(frame1, "Status: {}".format('Parking spot num 4 caught!'), (10, 100),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.6, (0, 0, 255), 1)
            ##if car leaving spot num 4
        if (x > 156 and x < 161) and (y > 185 and y < 190) and (catch_spot_num_4 == False):
            print(spot4Out)
            counterofspot4_out = counterofspot4_out + 1;  # counter of changes of frames at spot parking
            if counterofspot4_out > 2:
                avialibalrparkingspot = avialibalrparkingspot - 1;
                counterofspot4_out = 0;
                catch_spot_num_4 = True;
                cv2.putText(frame1, "Status: {}".format('Parking spot num 4 is available to park'), (10, 100),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.6, (0, 0, 255), 1)

            # Spots number 5 Checking
            # if car catch spot num 5
        if (x > 115 and x < 120) and (y > 150 and y < 155) and (catch_spot_num_5 == True):
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
        if (x > 115 and x < 120) and (y > 150 and y < 155) and (catch_spot_num_5 == False):
            print(spot5Out)
            counterofspot5_out = counterofspot5_out + 1;  # counter of changes of frames at spot parking
            if counterofspot5_out > 2:
                avialibalrparkingspot = avialibalrparkingspot - 1;
                counterofspot5_out = 0;
                catch_spot_num_5 = True;
                cv2.putText(frame1, "Status: {}".format('Parking spot num 5 is available to park'), (10, 100),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.6, (0, 0, 255), 1)

                # if car leaving the parking
        if (x>420 and x<641) and (y>370 and y<480):
            print(outallert)
            Leavingparking=True;
            cv2.putText(frame1, "Status: {}".format('Car/s leaving parking spot'), (50, 370), cv2.FONT_HERSHEY_SIMPLEX,
                        0.8, (0, 0, 255), 3)
            Exitparking=True;

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

    if cv2.waitKey(40) == 27:#Esc for exit camera
        break

cv2.destroyAllWindows()
cap.release()
out.release()



