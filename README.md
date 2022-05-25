Project description

I have attached an LED band to a breadboard connected to a RaspberryPi. I used a python script to turn on the led band, each led at a time.
Also, I have created an android companion app that opens/closes the led through http communication with the RaspberryPi.

Schematics, Setup and build

I have attached a mouse, keyboard and monitor to the RaspberryPi in order to program it. From the RaspberryPi I have connected one jumping
wire to power the breadboard (red). Next to it is our resistor, then 10 jumping wires ( red & orange) to power the led band. Then I connected 
the led band and next to it 10 more jumping wires ( multicolor: blue, white, purple, yellow, green) that control GPIO.
After I had finished the hardware setup, I wrote the python script to power the led band, each led at a time. Then I setup the RaspberryPi as a
server so that we can communicate with the android app through http get/post. I then wrote the android app using a simple interface with one 
button that serves both as power on and off. The app sends a request on button click that lets the RaspberryPi know it’s time to power the led.

Pre-requisites

The components are the following: 
-10k Ohm resistor 
-Breadboard and jumper wires https://www.optimusdigital.ro/ro/prototipare-breadboard-uri/8-breadboard-830-points.html?search_query=Breadboard&results=151, https://www.optimusdigital.ro/ro/fire-fire-mufate/878-set-fire-mama-tata-40p-30-cm.html?search_query=fire&results=435
-Jumper wires https://www.optimusdigital.ro/ro/fire-fire-mufate/884-set-fire-tata-tata-40p-10-cm.html?search_query=fire&results=435
-Raspberry Pi 3 Model B https://www.optimusdigital.ro/ro/placi-raspberry-pi/5091-raspberry-pi-3-model-b-plus.html?search_query=Raspberry+Pi+3+Model+B+&results=87
-MicroSD card for Raspberry Pi OS https://www.optimusdigital.ro/ro/memorii/11528-panasonic-card-microsd-a1-original-de-32-gb-cu-noobs-pentru-raspberry-pi-4.html?search_query=MicroSD&results=87
-LED band

Running

Once the hardware is connected, we have to power up the server on the RaspberryPi, then the android app and we are set to go.
