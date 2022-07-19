# Beacon-Project-Using-MQTT
An IOT Project that serves as a communication device for people in a workspace

The Beacon Project aims to establish a line of communication between professionals in a limited workplace. This device, while compact, will tend to the most basic of communications between colleagues, such as – recess, examinations, appraisals, etc. This interaction between the user and the device will be completely analogous and as simple as possible. Each individual will have one device and each of these devices will be connected to each other via the internet. This will enable a wireless form of communication. The design of the product will be compact, abstract, and straightforward. Each face of this device will be touch sensitive towards a specific function, and each face will have a different color for function recognizability. The functions of this device are as follows

-	Call for meeting (formal) – One face of this device will be a button dedicated to calling for a formal meeting

-	Call for meeting (informal) – An adjacent or opposite face would be a button dedicated towards an informal meeting

- Recess – One face to call or break for recess (tea, snacks, etc.)

-	Emergency face – Purely for untimely emergencies

-	Yes/No Face – Responses recorded with this face. Two buttons or a face divided into two. 

- Once a person calls for a particular function, an RGB strip at the base of the device turns into the color associated with that specific function. For example, if the formal meeting button is colored blue, once a person taps on it, all the other beacons will turn blue momentarily, until a response is received. 

- Reset – A tap on the button that is used to call a function cancels the function, i.e., to cancel or end a meeting, to end recess, etc. This function can be activated only by the person that calls for a particular meeting/function.

-	Lock – When a user calls for a meeting, every other beacon needs to turn inactive apart from the yes/no face so that no other beacon overrides the initial beacon’s function. Until the entire vote is completed, or the function is cancelled, all beacons stay passive.

##Hardware

###The Raspberry Pi
Raspberry Pi is a series of single board computers and enables the usage of a simple computer interface with a keyboard and mouse, and with added features of Scratch and Python. We initially began to use the Raspberry Pi 4 for the project but later moved on to use the Raspberry Pi Zero W, a smaller variant, which suited the size necessities for our project.

###Setting up the Pi
The Raspberry Pi requires an SD Card onto which we load the operating system Raspberry Pi OS (Previously known as Raspbian). We used a San Disk 16 GB SD Card for this purpose. The Raspberry Pi OS on the other hand can be installed from the official Raspberry Pi website. 
Once installed and initiated, the SD Card simply needs to be inserted into the appropriate slot on the Pi. 
For the Raspberry Pi 4, one could use it in any of the two ways we used it in.
- Using an HDMI cable, link up the Pi to a monitor and connect a keyboard and mouse to use.
- Download VNC Viewer on Windows/Mac OS and input the Raspberry Pi IP Address, connect both devices to the same Wi-Fi and use, akin to a remote monitor control.
For the Raspberry Pi Zero W, we install a specific file onto the OS loaded SD Card with Wi-Fi details so that the RaspPi Zero can connect to the specified Wi-Fi immediately on starting.

###Raspberry Pi Zero W
