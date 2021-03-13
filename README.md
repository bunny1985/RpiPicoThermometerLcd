# RpiPicoThermometerLcd
esp8266_i2c_lcd + ds18x20  + raspberry pico = kind of weather station

Needed: 

- raspberry pico flashed with micropython 
- esp8266 with I2C module 
- thermometer ds18x20
- 5 to 3 V logic converter 
- 5v power ( I used phone cable )


all needed libraries 

used pinout (lcd through converter) : 
LCD SCL -> pin 15 
LCD SDA -> pin 14 
thermoeter data -> pin 16 
thermomenter gnd to gnd , power to rpi power (3.3V)
LCD power directly from charger ( it uses 5V )

and basically thats it

![alt text](https://github.com/[username]/[reponame]/blob/[branch]/image.jpg?raw=true)






