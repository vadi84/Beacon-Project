from imp import lock_held
import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import board
import neopixel

client = mqtt.Client()
pixels = neopixel.NeoPixel(board.D18, 18)
ORDER = neopixel.GRB


def main():
    print("\t\t\tLED Program\n")
    print("Buttons:\tpin 18")  # RGB
    print("Buttons:\tpin 22")  # FM
    print("Buttons:\tpin 23")  # IFM
    print("Buttons:\tpin 24")  # EM
    print("Buttons:\tpin 25")  # REC
    print("Buttons:\tpin 26")  # 5th

    setupGPIO()
    no()
    global client
    try:
        client.loop_start()
        client.on_connect = on_connect
        client.on_message = on_message
        client.connect("broker.hivemq.com", 1883, 60)
        time.sleep(2)
        publisher()
    except:
        traceback.print_exc()
        quit(0)


def on_connect(client, userdata, flags, rc):
    print("Connected with a result code :" + str(rc))  # Subscribing and returning connect code
    client.subscribe("topic/touchsensor/pesu1")
    client.subscribe("topic/touchsensor/pesu2")
    client.subscribe("topic/touchsensor/pesu3")
    client.subscribe("topic/touchsensor/pesu4")
    client.subscribe("topic/touchsensor/pesu5")


def on_message(client, userdata, msg):
    global lock
    print("In on_message function")
    print(msg.payload)
    temp_varloop = False
    if msg.payload == b'meet':  # FORMAL MEETING
        #temp_varloop = False
        while (temp_varloop != True):
            print("On_Message")
            for x in range(0, 17):
                pixels[x] = (255,255, 255)  #WHITE
            time.sleep(1)
            for x in range(0,17):
                pixels[x]=(0,0,0)
            time.sleep(1)
            print("In On_message")
            if (GPIO.input(6) == True):  # NO
                no()
                print("NO")
                temp_varloop = True
            elif (GPIO.input(5) == True):  # YES
                print("YES")
                for x in range (0,17):
                    pixels[x]=(255,255,255)
                temp_varloop = True
            elif (GPIO.input(22) == True or GPIO.input(23) == True or GPIO.input(24) == True or GPIO.input(25) == True or GPIO.input(26)):
                print("Only Press YES or NO")
    elif msg.payload == b'meet_done':  # Terminating Formal Meeting
        print("TERMINATING FORMAL MEETING")
        for y in range(0,4):
            for x in range(0, 17):
                pixels[x] = (0, 0, 0)  # WHITE
            time.sleep(0.5)
            for x in range(0, 17):
                pixels[x] = (255, 255, 255)  # WHITE
            time.sleep(0.5)
        for x in range(0, 17):
            pixels[x] = (0, 0, 0)  # BLACK

    elif msg.payload == b'imeet':  # INFORMAL MEETING
        #temp_varloop = False
        while (temp_varloop != True):
            print("On_Message")
            for x in range(0, 17):
                pixels[x] = (90, 0, 255)  # LIGHT B
            time.sleep(1)
            for x in range(0, 17):
                pixels[x] = (0, 0, 0)  # LIGHT B
            time.sleep(1)

            print("In On_message")
            if (GPIO.input(6) == True):  # NO
                no()
                print("NO")
                temp_varloop = True
            elif (GPIO.input(5) == True):  # YES
                print("YES")
                for x in range (0,17):
                    pixels[x]=(90,0,255)
                temp_varloop = True
            elif (GPIO.input(22) == True or GPIO.input(23) == True or GPIO.input(24) == True or GPIO.input(25) == True or GPIO.input(26)):
                print("Only Press YES or NO")
    elif msg.payload == b'imeet_done':  # Terminating Informal Meeting
        print("TERMINATING INFORMAL MEETING")
        for y in range(0, 4):
            for x in range(0, 17):
                pixels[x] = (0, 0, 0)  # Light Blue
            time.sleep(0.5)
            for x in range(0, 17):
                pixels[x] = (90, 0, 255)  # Light Blue GRB
            time.sleep(0.5)
        for x in range(0, 17):
            pixels[x] = (0, 0, 0)  # Light Blue


    elif msg.payload == b'em':  # EMERGENCY MEETING
        #temp_varloop = False
        while (temp_varloop != True):
            print("On_Message")
            for x in range(0, 17):
                pixels[x] = (0, 255, 0)  # Red
            time.sleep(1)
            for x in range(0, 17):
                pixels[x] = (0, 0, 0)  # Red
            time.sleep(1)

            print("In On_message")
            if (GPIO.input(6) == True):  # NO
                no()
                temp_varloop = True
            elif (GPIO.input(5) == True):  # YES
                for x in range(0, 17):
                    pixels[x] = (0,255,0)  # RED
                temp_varloop =True
            elif (GPIO.input(22) == True or GPIO.input(23) == True or GPIO.input(24) == True or GPIO.input(25) == True or GPIO.input(26)):
                print("Only Press YES or NO")
    elif msg.payload == b'em_done':  # Terminating Emergency

        print("TERMINATING EMERGENCY")
        for y in range(0, 4):
            for x in range(0, 17):
                pixels[x] = (0, 0, 0)
            time.sleep(1)
            for x in range(0, 17):
                pixels[x] = (0, 255, 0)  # RED
            time.sleep(1)
        for x in range(0, 17):
            pixels[x] = (0, 0, 0)  # BLACK

    elif msg.payload == b'rec':  # RECESS
        #temp_varloop = False
        while (temp_varloop != True):
            print("On_Message")
            for x in range(0, 17):
                pixels[x] = (155, 255, 0)  # Orange
            time.sleep(1)
            for x in range(0, 17):
                pixels[x] = (0,0, 0)  # Orange
            time.sleep(1)

            print("In On_message")
            if (GPIO.input(6) == True):  # NO
                no()
                print("NO")
                temp_varloop = True
            elif (GPIO.input(5) == True):  # YES
                print("YES")
                for x in range(0, 17):
                    pixels[x] = (155, 255, 0)  # Orange
                temp_varloop = True
            elif (GPIO.input(22) == True or GPIO.input(23) == True or GPIO.input(24) == True or GPIO.input(25) == True or GPIO.input(26)):
                print("Only Press YES or NO")
    elif msg.payload == b'rec_done':  # Terminating Recess
        print("TERMINATING RECESS")
        for y in range(0, 4):
            for x in range(0, 17):
                pixels[x] = (0, 0, 0)  # Orange
            time.sleep(1)
            for x in range(0, 17):
                pixels[x] = (155, 255, 0)  # Orange
            time.sleep(1)
        for x in range(0, 17):
            pixels[x] = (0, 0, 0)  # Black

    elif msg.payload == b'party':  # RF5
        #temp_varloop = False
        while (temp_varloop != True):
            print("On_Message")
            for x in range(0, 17):
                pixels[x] = (0, 255, 255)  # Purple
            time.sleep(1)
            for x in range(0, 17):
                pixels[x] = (0, 0, 0)  # Purple
            time.sleep(1)

            print("In On_message")
            if (GPIO.input(6) == True):  # NO
                no()
                print("NO")
                temp_varloop = True
            elif (GPIO.input(5) == True):  # YES
                print("YES")
                for x in range (0,17):
                    pixels[x]=(0,255,255)
                temp_varloop = True
            elif (GPIO.input(22) == True or GPIO.input(23) == True or GPIO.input(24) == True or GPIO.input(25) == True or GPIO.input(26)):
                print("Only Press YES or NO")
    elif msg.payload == b'party_done':  # Terminating f5
        print("TERMINATING FUNCTION 5")
        for y in range(0, 4):
            for x in range(0, 17):
                pixels[x] = (0, 0, 0)  # Purple
            time.sleep(1)
            for x in range(0, 17):
                pixels[x] = (0, 255, 255)  # Purple
            time.sleep(1)
        for x in range(0, 17):
            pixels[x] = (0, 0, 0)  # Black


def setupGPIO():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Recess
    GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Formal Meeting
    GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Informal Meeting
    GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Emergency
    GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Party
    GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # YES
    GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # NO


def no():
    for x in range(0, 17):
        pixels[x] = (0, 0, 0)



def publisher():
    global client
    while True:
        print("In Publisher")
        #print(GPIO.Input(26))
        time.sleep(1)
        if (GPIO.input(22) == True):
            print("Verify")
            client.loop_stop()
            publish.single("topic/touchsensor/pesu1", "meet", hostname="broker.hivemq.com")
            for x in range(0, 17):
                pixels[x] = (255, 255, 255)  # WHITE
            while (GPIO.input(22) != True):
                print("Formal Meeting in progress\n")
            publish.single("topic/touchsensor/pesu1", "meet_done", hostname="broker.hivemq.com")
            for x in range(0, 17):
                pixels[x] = (0, 0, 0)  #OFF
            main()
            
        elif (GPIO.input(23) == True):
            print("Verify")
            client.loop_stop()
            publish.single("topic/touchsensor/pesu2", "imeet", hostname="broker.hivemq.com")
            for x in range(0, 17):
                pixels[x] = (90, 0, 255)  # LIGHT BLUE
            while (GPIO.input(23) != True):
                print("Informal Meeting in progress\n")
            publish.single("topic/touchsensor/pesu2", "imeet", hostname="broker.hivemq.com")
            for x in range(0, 17):
                pixels[x] = (0, 0, 0)  # OFF
            main()

        elif (GPIO.input(24) == True):  # Emergency
            print("Verify")
            client.loop_stop()
            publish.single("topic/touchsensor/pesu3", "em", hostname="broker.hivemq.com")
            for x in range(0, 17):
                pixels[x] = (0, 255,0)  #RED
            while (GPIO.input(24) != True):
                print("Emergency in progress\n")
            publish.single("topic/touchsensor/pesu3", "em_done", hostname="broker.hivemq.com")
            for x in range(0, 17):
                pixels[x] = (0, 0, 0)  # Off
            main()

        elif (GPIO.input(25) == True):  # Recess
            print("Verify")
            client.loop_stop()
            publish.single("topic/touchsensor/pesu4", "rec", hostname="broker.hivemq.com")
            for x in range(0, 17):
                pixels[x] = (155, 255, 0)  # ORANGE
            while (GPIO.input(25) != True):
                print("Recess in progress\n")
            publish.single("topic/touchsensor/pesu4", "rec_done", hostname="broker.hivemq.com")
            for x in range(0, 17):
                pixels[x] = (0, 0, 0)  # OFF
            main()

        elif (GPIO.input(26) == True):  # 5th
            print("Verify")
            client.loop_stop()
            publish.single("topic/touchsensor/pesu5", "party", hostname="broker.hivemq.com")
            for x in range(0, 17):
                pixels[x] = (0, 255, 255)  # PURPLE
            time.sleep(1)
            while (GPIO.input(26) != True):
                print("F5 in progress\n")
            publish.single("topic/touchsensor/pesu5", "party_done", hostname="broker.hivemq.com")
            for x in range(0, 17):
                pixels[x] = (0, 0, 0)  # OFF
            main()


if __name__ == "__main__":
    main()
GPIO.cleanup()
