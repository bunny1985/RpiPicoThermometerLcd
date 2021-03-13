from esp8266_i2c_lcd import I2cLcd
import lcd_api
import machine, onewire, ds18x20, time

print("Let's start")
print("setup LCD")
i2c_lcd = machine.I2C(1, sda=machine.Pin(14), scl=machine.Pin(15), freq=400000)

lcd = I2cLcd(i2c_lcd, 0x27, 2, 16)
lcd.clear()
lcd.putstr("Start LCD!")

time.sleep(1.0)

print("LCD should be ok")

print("preparing thermometer")
lcd.clear()
lcd.putstr("Ustawiam\ntermomentr")

ds_pin = machine.Pin(16)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))

roms = ds_sensor.scan()
print('Found a ds18x20 device')
lcd.clear()
lcd.putstr("Termometr\ngotowy")
time.sleep(1.0)
lcd.clear()
lcd.putstr("Zaczynam\nliczyć temp.")
time.sleep(1.0)
lcd.clear()
lcd.putstr("Temperatura")

while True:
    ds_sensor.convert_temp()
    time.sleep_ms(750)
    for rom in roms:
        temp = ds_sensor.read_temp(rom)
        print(ds_sensor.read_temp(rom))
        lcd.move_to(0, 1)
        lcd.putstr("{:.2f} C".format(temp))
    time.sleep(0.5)

