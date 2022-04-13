# Making-a-digital-clock-and-syncing-it-with-my-phone
For this project i'm using circuit python and i'm working with the [ADAFRUIT 1.12 OLED DISPLAY](https://cdn-learn.adafruit.com/downloads/pdf/adafruit-monochrome-1-12-in-128x128-oled.pdf)
, [Feather nRf54820](https://www.adafruit.com/product/4062) and ill also be using a wifi module.
Phones are showing you the right time thanks to being constantly synchronized with the atomic clocks via cell towers, via internet, and via GPS etc. Now if the digital clock
im making is also in sync with the following then its also in sync with my phone. If there is any noticable offset then I know i went wrong.
keeping this general idea in mind im working on it

I'm diving this into two parts for simplicity
  1. making the digital clock itself
- using I2C interfacing diplay and MC
- writing code to display whatever i want
- displaying accturate time using WIFI module?

  2.Using [BlueFRUIT](https://learn.adafruit.com/circuitpython-nrf52840/overview) 
  - send data( that is time on my digital clock ) using BLE and display that on my phone through the app
  - check for offest and conclue that its synced.
  
....i'll be writing more this is just a draft......
  
  ---- feather_fruit >-<
