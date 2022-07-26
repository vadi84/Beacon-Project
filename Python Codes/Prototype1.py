from imp import lock_held
import Rpi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import board
import neopixel

#led_on = False
client = mqtt.Client()
pixels=neopixel.Neopixel(board,D18,18)
ORDER = neopixel.RGB

def main():
    print("\t\t\tLED Program\n")
    print("LED:\tpin 18")
    print("Buttons:\tpin 21") #RGB
    print("Buttons:\tpin 22") #FM
    print("Buttons:\tpin 23") #IFM
    print("Buttons:\tpin 24") #EM   
    print("Buttons:\tpin 25") #REC
    print("Buttons:\tpin 26") #5th   


    setupGPIO()
    global client
    try:
        client.loop_start()
        client.on_connect = on_connect()
        client.on_message = on_message()
        client.connect("broker.hivemq.com", 1883,60)
        time.sleep(2)
        publisher()
        time.sleep(2)
    except:
        traceback.print_exc()
        quit(0)

def on_connect(client, userdata, flags, rc):
    print("Connected with a result code :" + str(rc)) #Subscribing and returning connect code
    client.subscribe("topic/touchsensor/pesu1")
    client.subscribe("topic/touchsensor/pesu2")
    client.subscribe("topic/touchsensor/pesu3")
    client.subscribe("topic/touchsensor/pesu4")
    client.subscribe("topic/touchsensor/pesu5")


def on_message(client, userdata, msg):
    global lock
    print("In on_message function")
    print(msg.payload)
    temp_varloop =  False
    if msg.payload == b'meet': #FORMAL MEETING
        print("Light Blue")
        while(temp_varloop!=True):
            print("On_Message")
            for x in range (0,17):
                pixels[x] = (0,0,0) #Light Blue
            time.sleep(2)
            print("In On_message")
            if(GPIO.input(6)==True): #NO
                no()
                temp_varloop=True
            elif(GPIO.input(5)==True): #YES
                yes()
                temp_varloop==True
            elif{(GPIO.input(23)==True) || (GPIO.input(24)==True) || (GPIO.input(25)==True) || (GPIO.input(26)==True)}:
                print("Only Press YES or NO")
    elif msg.payload == b'meet_done': #Terminating Formal Meeting
        for x in range (0,17):
            pixels[x] = (0,0,0) #Light Blue
        time.sleep(2)

    elif msg.payload == b'imeet': #INFORMAL MEETING
        print("Light Green")
        while(temp_varloop!=True):
            print("On_Message")
            for x in range (0,17):
                pixels[x] = (0,0,0) #Light Blue
            time.sleep(2)

            print("In On_message")
            if(GPIO.input(6)==True): #NO
                no()
                temp_varloop=True
            elif(GPIO.input(5)==True): #YES
                yes()
                temp_varloop==True
            elif(GPIO.input(22)==True || GPIO.input(24)==True || GPIO.input(25)==True || GPIO.input(26)==True ):
                print("Only Press YES or NO")
    elif msg.payload == b'imeet_done': #Terminating Informal Meeting
        for x in range (0,17):
            pixels[x] = (0,0,0) #Light Green
        time.sleep(2)

    
    elif msg.payload == b'em': #EMERGENCY MEETING
        print("Red")
        while(temp_varloop!=True):
            print("On_Message")
            for x in range (0,17):
                pixels[x] = (0,0,0) #Red
            time.sleep(2)

            print("In On_message")
            if(GPIO.input(6)==True): #NO
                no()
                temp_varloop=True
            elif(GPIO.input(5)==True): #YES
                yes()
                temp_varloop==True
            elif(GPIO.input(22)==True || GPIO.input(23)==True || GPIO.input(25)==True || GPIO.input(26)==True ):
                print("Only Press YES or NO")
    elif msg.payload == b'em_done': #Terminating Emergency
        for x in range (0,17):
            pixels[x] = (0,0,0) #Red
        time.sleep(2)


    elif msg.payload == b'rec': #RECESS
        print("Orange")
        while(temp_varloop!=True):
            print("On_Message")
            for x in range (0,17):
                pixels[x] = (0,0,0) #Orange
            time.sleep(2)

            print("In On_message")
            if(GPIO.input(6)==True): #NO
                no()
                temp_varloop=True
            elif(GPIO.input(5)==True): #YES
                yes()
                temp_varloop==True
            elif(GPIO.input(22)==True || GPIO.input(23)==True || GPIO.input(24)==True || GPIO.input(26)==True ):
                print("Only Press YES or NO")
    elif msg.payload == b'rec_done': #Terminating Recess
        for x in range (0,17):
            pixels[x] = (0,0,0) #Orange
        time.sleep(2)

    elif msg.payload == b'Function5': #RF5
        print("Purple")
        while(temp_varloop!=True):
            print("On_Message")
            for x in range (0,17):
                pixels[x] = (0,0,0) #Purple
            time.sleep(2)

            print("In On_message")
            if(GPIO.input(6)==True): #NO
                no()
                temp_varloop=True
            elif(GPIO.input(5)==True): #YES
                yes()
                temp_varloop==True
            elif(GPIO.input(22)==True || GPIO.input(23)==True || GPIO.input(24)==True || GPIO.input(25)==True ):
                print("Only Press YES or NO")
    elif msg.payload == b'rf5_done': #Terminating f5
        for x in range (0,17):
            pixels[x] = (0,0,0) #Purple
        time.sleep(2)

def setupGPIO():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(21, GPIO.OUT, initial=GPIO.LOW)#RGB Strip
    GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP)#Recess
    GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)#Formal Meeting
    GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)#Informal Meeting
    GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)#Emergency
    GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)#Fifth Function
    GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)#YES
    GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)#NO

def yes():
    while True:
            for x in range (0,17):
                pixels[x] = (0,0,0) #White
            time.sleep(2)
def no():
    while True:
            for x in range (0,17):
                pixels[x] = (0,0,0) #White
            time.sleep(2)



def publisher():
    global client
    while (True):
        print("In Publisher")
        print(GPIO.Input(26))
        time.sleep(1)
        if(GPIO.input(26)==True):
            print("Verify")
            client.loop_stop()
            publish.single("topic/touchsensor/pesu1","meet",hostname="broker.hivemq.com")
            for x in range (0,17):
                pixels[x] = (0,0,0) #Colour
            time.sleep(2)
            while(GPIO>input(26)!=True):
                print("Formal Meeting in progress\n")
                time.sleep(1)
            publish.single("topic/touchsensor/pesu1","meet_done",hostname="broker.hivemq.com")
            for x in range (0,17):
                pixels[x] = (0,0,0) #Off
            time.sleep(2)
            main()
        elif(GPIO.input(27)==True):
            print("Verify")
            client.loop_stop()
            publish.single("topic/touchsensor/pesu2 ","imeet",hostname="broker.hivemq.com")
            for x in range (0,17):
                pixels[x] = (0,0,0) #Colour
            time.sleep(2)
            while(GPIO>input(27)!=True):
                print("Informal Meeting in progress\n")
                time.sleep(1)
            publish.single("topic/touchsensor/pesu2","imeet_done",hostname="broker.hivemq.com")
            for x in range (0,17):
                pixels[x] = (0,0,0) #Off
            time.sleep(2)
            main()
        elif(GPIO.input(28)==True): #Emergency
            print("Verify")
            client.loop_stop()
            publish.single("topic/touchsensor/pesu3 ","em",hostname="broker.hivemq.com")
            for x in range (0,17):
                pixels[x] = (0,0,0) #Colour
            time.sleep(2)
            while(GPIO>input(28)!=True):
                print("Emergency in progress\n")
                time.sleep(1)
            publish.single("topic/touchsensor/pesu3","em_done",hostname="broker.hivemq.com")
            for x in range (0,17):
                pixels[x] = (0,0,0) #Off
            time.sleep(2)
            main()
        elif(GPIO.input(25)==True): #Recess
            print("Verify")
            client.loop_stop()
            publish.single("topic/touchsensor/pesu4 ","rec",hostname="broker.hivemq.com")
            for x in range (0,17):
                pixels[x] = (0,0,0) #Colour
            time.sleep(2)
            while(GPIO>input(25)!=True):
                print("Recess in progress\n")
                time.sleep(1)
            publish.single("topic/touchsensor/pesu4","rec_done",hostname="broker.hivemq.com")
            for x in range (0,17):
                pixels[x] = (0,0,0) #Off
            time.sleep(2)
            main()
        elif(GPIO.input(25)==True): #Recess
            print("Verify")
            client.loop_stop()
            publish.single("topic/touchsensor/pesu5 ","f5",hostname="broker.hivemq.com")
            for x in range (0,17):
                pixels[x] = (0,0,0) #Colour
            time.sleep(2)
            while(GPIO>input(25)!=True):
                print("F5 in progress\n")
                time.sleep(1)
            publish.single("topic/touchsensor/pesu5","f5_done",hostname="broker.hivemq.com")
            for x in range (0,17):
                pixels[x] = (0,0,0) #Off
            time.sleep(2)
            main()

if __name__ == "__main__":
    main()
#GPIO Cleanup

    
    
