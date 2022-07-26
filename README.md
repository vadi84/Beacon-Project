# Beacon-Project-Using-MQTT
An IOT Project that serves as a communication device for people in a workspace.

The Beacon Project aims to establish a line of communication between professionals in a limited workplace. This device, while compact, will tend to the most basic of communications between colleagues, such as – recess, examinations, appraisals, etc. This interaction between the user and the device will be completely analogous and as simple as possible. Each individual will have one device and each of these devices will be connected to each other via the internet. This will enable a wireless form of communication. The design of the product will be compact, abstract, and straightforward. Six faces of this device will have slots for a touch sensor, each with specific function and a different color for function recognizability. The functions of this device are as follows

-	Call for meeting (formal) – One face of this device will be a button dedicated to calling for a formal meeting

-	Call for meeting (informal) – An adjacent or opposite face would be a button dedicated towards an informal meeting

- Recess – One face to call or break for recess (tea, snacks, etc.)

-	Emergency face – Purely for untimely emergencies

- Party face 

-	Yes/No Face – Responses recorded with this face. Two slots in a face, one for each of Yes and No 

- Once a person calls for a particular function, an RGB strip at the base of the device turns into the color associated with that specific function. For example, if the formal meeting button is colored blue, once a person taps on it, all the other beacons will flash blue momentarily, until a response is received. 

- Reset – A tap on the sensor that is used to call a function cancels the function, i.e., to cancel or end a meeting, to end recess, etc. This function can be activated only by the person that calls for a particular meeting/function.

-	Lock – When a user calls for a meeting, every other beacon needs to turn inactive apart from the yes/no face so that no other beacon overrides the initial beacon’s function. Until the entire vote is completed, or the function is cancelled, all beacons stay passive.
<br>
<br>
<br>

## **Hardware** ##

### The Raspberry Pi
Raspberry Pi is a series of single board computers and enables the usage of a simple computer interface with a keyboard and mouse, and with added features of Scratch and Python. We initially began to use the Raspberry Pi 4 for the project but later moved on to use the Raspberry Pi Zero W, a smaller variant, which suited the size necessities for our project.
<br>
<br>
### _Setting up the Pi_
The Raspberry Pi requires an SD Card onto which we load the operating system Raspberry Pi OS (Previously known as Raspbian). We used a San Disk 16 GB SD Card for this purpose. The Raspberry Pi OS on the other hand can be installed from the official Raspberry Pi website. 
Once installed and initiated, the SD Card simply needs to be inserted into the appropriate slot on the Pi. 
For the Raspberry Pi 4, one could use it in any of the two ways we used it in.
- Using an HDMI cable, link up the Pi to a monitor and connect a keyboard and mouse to use.
- Download VNC Viewer on Windows/Mac OS and input the Raspberry Pi IP Address, connect both devices to the same Wi-Fi and use, akin to a remote monitor control.
For the Raspberry Pi Zero W, we install a specific file onto the OS loaded SD Card with Wi-Fi details so that the RaspPi Zero can connect to the specified Wi-Fi immediately on starting.
<br>
<br>

#### _Running the Pi on startup_
To run the Raspberry Pi on startup, we use the ``rc.local`` method, most likely the easiest and simplest way to get your program to run on boot. The downside is that tasks started with rc.local happen before the X windows system starts, which means you will not have access to graphical user interface (GUI) elements.

You will need root-level access to modify rc.local, so do so with sudo: ``sudo nano /etc/rc.local``
Scroll down, and just before the exit 0 line, enter the following: ``python /home/file_address/codename.py &`` 

Test by saving with ctrl+x and reboot your Pi.

The quickest way to stop your program is to kill its Linux process. In a terminal, enter the following command: ``sudo ps -ax | grep python``
Then, find the process ID (PID) number to the left of the listed process, and use the kill command to terminate that process: ``sudo kill <PID>``

<br>
<br>


### _Raspberry Pi Zero W_

The RaspPi Zero W has the following features - <br>
•	1GHz single-core ARMv6 CPU (BCM2835) <br>
•	VideoCore IV GPU, 512MB RAM <br>
•	Mini HDMI and USB on-the-go ports <br>
•	Micro USB power <br>
•	HAT-compatible 40-pin header <br>
•	Composite video and reset headers <br>
•	CSI camera connector <br>
•	802.11n wireless LAN <br>
•	Bluetooth 4.0 <br>
<br>
<br>
## Elements of the project ##

### _Establishing Inter-device communication using the MQTT protocol_ ###

MQTT is an OASIS standard messaging protocol for the Internet of Things (IoT). It is designed as an extremely lightweight publish/subscribe messaging transport that is ideal for connecting remote devices with a small code footprint and minimal network bandwidth. 
MQTT eliminates the standard client-server relationship and establishes a client-broker scene wherein every device in this network can either _publish_ data on a particular _topic_ or read published data by _subscribing_ to said topic, with the broker acting as a middle man. This maintains efficiency, light weightedness, and scalability in communication.
<br>
<br>
<br>
#### _Installation_ ####

To install MQTT on the Raspberry Pi, we take the following steps:
 1. Before installing the MQTT broker, update the Raspberry Pi OS using either of the following two commands in the Rasp Pi OS Terminal

`` sudo apt upgrade `` <br>
`` sudo apt update ``  <br>

 2. Once updated, we can install the MQTT software using the following commands

`` sudo apt install mosquitto mosquitto-clients `` <br>

 3. To verify the installation, type

`` sudo <your system name> status mosquitto `` <br>
<br>
<br>
<br>
<br>
#### _Establishing a connection_ ####

To establish the connection and create a broker with MQTT, we use python <br>

The following are essential towards initiating the broker setup and setting the CONNECT and CONNACK betweek the client and broker.
The core of the client library is the client class which provides all of the functions to publish messages and subscribe to topics.

To use the client class, import it using ``import paho.mqtt.client as mqtt`` 

``client = mqtt.Client(client_name)`` is used to create an instance 

Before you can publish messages or subscribe to topics you need to establish a connection to a broker. To do this, use the connect method of the Python MQTT client. This method can be called with 4 parameters. The connect method declaration is shown below with the default parameters.

``connect(host, port=1883, keepalive=60, bind_address="")`` <br>

In our code, we use the HiveMQ free broker, and hence we type it as ``client.connect("broker.hivemq.com", 1883, 60)`` <br>
<br>
<br>
<br>
<br>
#### _Callbacks, CONNECT, and CONNACK_ ####

Callbacks are functions that are called in response to an event. Event Connection acknowledged Triggers the ``on_connect`` callback. Event Message Received Triggers the ``on_message`` callback.

When the client receives a CONNACK message the callback is triggered if it exists.

These callback functions are used only if they exist in the code, there are no default functions available. Callbacks are dependent on something called a client loop as without the loop the callbacks aren’t triggered. The ``loop()`` function is a built in function that will read the receive and send buffers, and process any messages it finds.

``client.loop_start()`` starts the client loop and searches for callbacks
``client.loop_stop()`` terminates the loop

For our project, we required the code to subscribe to the required topics for each of the functions, hence an on_connect function that needs to subscribe to topics roughly looks like this:

```
def on_connect(client, userdata, flags, rc):
    print("Connected with a result code :" + str(rc))  # Subscribing and returning connect code
    client.subscribe("topic/topicname")
```
    
Now, to associate this with the client object, we type

``client.on_connect() = on_connect()`` <br>

Our on_message function comprised of commands that controlled the RGB LED Strips on responses via the touch sensors on the device. If a particular touch sensor would be touched, that would trigger a particular message to be published on the function topic. on_message would check for this message and the state of the sensor with a few if-else statements and accordingly control the hardware

The following is a rough depiction of the on_message function for our case:

```
def on_message(client, userdata, msg):
    print(msg.payload) #msg.payload carries the published message info
    if message = call a meeting
         Flash LED
    Check for YES or NO sensor response 
    if YES
         Flash LED
    if NO
         Terminate
 ```
<br>
<br>
<br>
<br>

#### _Publishing a Message on a Topic_ ####

To publish information, we must first import the publish library with ``import paho.mqtt.publish as publish``

Publishing information onto a topic is relatively straightforward. Create a publisher function which you can call everytime required and define the function content.

It is important to note that to publish information, the client loop must be stopped using ``client.loop_stop()``. To publish a message on a topic, the following syntax is followed:

``publish.single("topic/topicname", "Message_to_be_published", hostname="broker.hivemq.com")``
<br>
<br>
<br>
<br>
#### _Setting up and controlling GPIO Pins_ ####

GPIO stands for General Purpose Input Output. The Raspberry Pi Zero W has two rows of 40 pins, consisting of pins for DC power, grounding, and GPIO (27 pins) and more. 

To access and use sensors/circuits connected to these GPIO pins, we need to first import the GPIO library using ``import RPi.GPIO as GPIO``  <br>
RPi.GPIO supports referring to GPIO pins using the physical pin numbers.

GPIO High and Low are the basic levels of communication between sensors connected to these pins and the board. 

To set up a channel as an input or an output, call either: ``GPIO.setup(channel, GPIO.IN)`` or ``GPIO.setup(channel, GPIO.OUT)``

To read the value of an input channel, call ``GPIO.input(channel)`` and to declare the value on a channel, call ``GPIO.output(channel,state)``

To access and enable these pins it is also necessary to set these pins up using the ``setupGPIO()`` function. This function will consist of the following syntax

```
def setupGPIO():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(GPIO_pin_number, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Enables a pull up/pull down
```

<br>

#### _Touch Sensors_ ####

The touch sensors that we used for the project are the TTP223B Touch Sensors. These sensors have 3 ports - 
 - **SIG** : To be connected to a GPIO pin
 - **VCC** : To be connected to a DC power supply
 - **GND** : To be grounded

<br>
<br>
<br>
<br>

#### _RGB LED Strip_ ####

To use the RGB LED Strip (WS2812B), we first need to import the required libraries using ``import board`` and ``import neopixel``

``pixels = neopixel.NeoPixel(board.D18, 18)`` initiates the LED strip to pin 18. 
``ORDER = neopixel.GRB`` declares the order of colour encoding as GRB.

``pixels[node_number] = (255,255,255)`` is the syntax to control the colour emitted by the LED strip.

To flash the LED, we use
```
for x in range(0, 17):
    pixels[x] = (255,255, 255)  #WHITE
    time.sleep(1)
for x in range(0,17):
    pixels[x]=(0,0,0)
```
To turn the strip off, control the strip colour to black (0,0,0).
<br>
<br>

#### _Modelling the project_ ####

The shape we selected for our model was a dodecahedron (12-uniformly-sided 3D figure). <br>
Software used: Autodesk Fusion360 <br>

We split the model into 2 halves to make the 3D printing process simpler. Find the .stl files attached to this repository.

## **END** ##


