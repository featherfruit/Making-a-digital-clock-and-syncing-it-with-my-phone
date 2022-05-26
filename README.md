## **A DIGITAL CLOCK + SERVER THAT GIVES U (TIME) OFFSET**
this is a little project where, I made a Digital Clock and a web server that tells you whats the time on the digital clock and lets you syncronise the time with the clock and gives you offset if there is any.


### Making the Digital clock
Firstly you need to set up your rasberry pi and install a bunch of thing. I'm using a Rasberry Pi 4B. This [guide](https://circuitdigest.com/microcontroller-projects/ssd1306-oled-display-with-raspberry-pi ) should be helpful. I've
taken code from there and modified it according my requirments.
the raspi and oled communicate using simple i2c.

### Server
Using Flask a web framawork written in python we've created a simple web application that takes time
from your device and takes time displayed on the clock that is the accurate time from the rasberry pi's OS and calculates the offset and returns it to you.
So its an application where input is taken from the user and based on it data is displayed back on the HTML.
S
### Shell Scripts 
Scripts to start displaying time and run the web server at boot





#### Useful resources

https://flask.palletsprojects.com/en/1.0.x/patterns/streaming/

https://stackoverflow.com/questions/53111362/fun-clock-streaming-text-with-python-and-flask

https://stackoverflow.com/questions/51669102/how-to-pass-data-to-html-page-using-flask

https://www.guru99.com/introduction-to-shell-scripting.html
