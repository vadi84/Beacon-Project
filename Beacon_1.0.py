from imp import lock_held
import Rpi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import board
import neopixel
import time 


pixels=neopixel.Neopixel(board,D18,18)
led_on = False
client = mqtt.Client()

def main():
    print("\t\t\tLED Program\n")
    print("LED:\tpin 4")
    print("Button:\tpin 26")

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


def on_message(client, userdata, msg):
    global lock
    print("In on_message function")
    print(msg.payload)
    temp_varloop =  False
    if msg.payload == b'meet': #FORMAL MEETING
        print("LED Flash")
        while(temp_varloop!=True):
            print("On_Message")
            flashLED(5)
            print("In On_message")
            if(GPIO.input(6)==True): #NO
                no()
                temp_varloop=True
            elif(GPIO.input(5)==True): #YES
                yes()
                temp_varloop==True
            elif{(GPIO.input(26)==True) || (GPIO.input(27)==True) || (GPIO.input(28)==True)}:
                print("Only Press YES or NO")
    elif msg.payload == b'meet_done': #Terminating Formal Meeting
        flashLED(5)
        GPIO.output(4, GPIO.LOW)

    if msg.payload == b'imeet': #INFORMAL MEETING
        print("LED Flash")
        while(temp_varloop!=True):
            print("On_Message")
            flashLED(5)
            print("In On_message")
            if(GPIO.input(6)==True): #NO
                no()
                temp_varloop=True
            elif(GPIO.input(5)==True): #YES
                yes()
                temp_varloop==True
            elif(GPIO.input(26)==True || GPIO.input(27)==True || GPIO.input(28)==True):
                print("Only Press YES or NO")
    elif msg.payload == b'imeet_done': #Terminating Informal Meeting
        flashLED(5)
        GPIO.output(4, GPIO.LOW)
    
    if msg.payload == b'em': #EMERGENCY MEETING
        print("LED Flash")
        while(temp_varloop!=True):
            print("On_Message")
            flashLED(5)
            print("In On_message")
            if(GPIO.input(6)==True): #NO
                no()
                temp_varloop=True
            elif(GPIO.input(5)==True): #YES
                yes()
                temp_varloop==True
            elif(GPIO.input(26)==True || GPIO.input(27)==True || GPIO.input(28)==True):
                print("Only Press YES or NO")
    elif msg.payload == b'em_done': #Terminating Emergency
        flashLED(5)
        GPIO.output(4, GPIO.LOW)

    if msg.payload == b'rec': #RECESS
        print("LED Flash")
        while(temp_varloop!=True):
            print("On_Message")
            flashLED(5)
            print("In On_message")
            if(GPIO.input(6)==True): #NO
                no()
                temp_varloop=True
            elif(GPIO.input(5)==True): #YES
                yes()
                temp_varloop==True
            elif(GPIO.input(26)==True || GPIO.input(27)==True || GPIO.input(28)==True):
                print("Only Press YES or NO")
    elif msg.payload == b'rec_done': #Terminating Recess
        flashLED(5)
        GPIO.output(4, GPIO.LOW)
        

def setupGPIO():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(4, GPIO.OUT, initial=GPIO.LOW)#LED
    GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP)#Recess
    GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)#Formal Meeting
    GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)#Informal Meeting
    GPIO.setup(28, GPIO.IN, pull_up_down=GPIO.PUD_UP)#Emergency
    GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)#YES
    GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)#NO

def yes():
    print("YES")
    GPIO.output(4,GPIO.HIGH)
def no():
    print("NO")
    GPIO.output(4,GPIO.LOW)

def flashLED(count):
    for i in range(count):
        GPIO.output(4, GPIO.HIGH)
        time.sleep(0.15)
        GPIO.output(4,GPIO.LOW)
        time.sleep(0.15)

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
            flashLED(5)
            GPIO.output(4,GPIO.HIGH)
            while(GPIO>input(26)!=True):
                print("Formal Meeting in progress\n")
                time.sleep(1)
            publish.single("topic/touchsensor/pesu1","meet_done",hostname="broker.hivemq.com")
            flashLED(5)
            GPIO.output(4, GPIO.LOW)
            main()
        elif(GPIO.input(27)==True):
            print("Verify")
            client.loop_stop()
            publish.single("topic/touchsensor/pesu2 ","imeet",hostname="broker.hivemq.com")
            flashLED(5)
            GPIO.output(4,GPIO.HIGH)
            while(GPIO>input(27)!=True):
                print("Formal Meeting in progress\n")
                time.sleep(1)
            publish.single("topic/touchsensor/pesu2","imeet_done",hostname="broker.hivemq.com")
            flashLED(5)
            GPIO.output(4, GPIO.LOW)
            main()
        elif(GPIO.input(28)==True): #Emergency
            print("Verify")
            client.loop_stop()
            publish.single("topic/touchsensor/pesu3 ","em",hostname="broker.hivemq.com")
            flashLED(5)
            GPIO.output(4,GPIO.HIGH)
            while(GPIO>input(28)!=True):
                print("Formal Meeting in progress\n")
                time.sleep(1)
            publish.single("topic/touchsensor/pesu3","em_done",hostname="broker.hivemq.com")
            flashLED(5)
            GPIO.output(4, GPIO.LOW)
            main()
        elif(GPIO.input(25)==True): #Recess
            print("Verify")
            client.loop_stop()
            publish.single("topic/touchsensor/pesu4 ","rec",hostname="broker.hivemq.com")
            flashLED(5)
            GPIO.output(4,GPIO.HIGH)
            while(GPIO>input(25)!=True):
                print("Formal Meeting in progress\n")
                time.sleep(1)
            publish.single("topic/touchsensor/pesu4","rec_done",hostname="broker.hivemq.com")
            flashLED(5)
            GPIO.output(4, GPIO.LOW)
            main()

if __name__ == "__main__":
    main()
#GPIO Cleanup

'''while True:
for x in range (0,17):
pixels[x] = (0,0,0)
time.sleep(2)'''
    
