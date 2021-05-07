"""
To get started, check out the "Device Simulator Express: Getting Started" command in the command pallete, which you can access with `CMD + SHIFT + P` For Mac and `CTRL + SHIFT + P` for Windows and Linux.

To learn more about the CLUE and CircuitPython, check this link out:
https://learn.adafruit.com/adafruit-clue/circuitpython

Find example code for CPX on:
https://blog.adafruit.com/2020/02/12/three-fun-sensor-packed-projects-to-try-on-your-clue-adafruitlearningsystem-adafruit-circuitpython-adafruit/
"""
from adafruit_clue import clue
import paho.mqtt.client as mqtt


def display_text(clueValue): #to display the value of the clue in the screen
    clue_data[0].text = "Accel: {} {} {} m/s^2".format(*(clueValue["clueSlider/accelXRange"], clueValue["clueSlider/accelYRange"], clueValue["clueSlider/accelZRange"])) #display pink color text accel with its specific X,Y,Z range value in data 0
    clue_data[1].text = "Gyro: {} {} {} dps".format(*(clueValue["clueSlider/gyroXRange"], clueValue["clueSlider/gyroYRange"], clueValue["clueSlider/gyroZRange"])) #display green color text gyro with its specific X,Y,Z range value in data 1
    clue_data[2].text = "Magnetic: {} {} {} uTesla".format(*(clueValue["clueSlider/magneticXRange"], clueValue["clueSlider/magneticYRange"], clueValue["clueSlider/magneticZRange"])) #display red color text magnetic with its specific X,Y,Z range value in data 2
    clue_data[3].text = "Pressure: {} hPa".format(clueValue["clueSlider/pressureRange"]) #dispaly sky color text pressure with its format range value in data 3
    clue_data[4].text = "Temperature: {} C".format(clueValue["clueSlider/tempRange"]) #dispaly color text temperature with its format range value in data 4
    clue_data[5].text = "Humidity: {} %".format(clueValue["clueSlider/humidityRange"]) #dispaly color blue text humidity with its format range value in data 5
    clue_data[6].text = "Proximity: {}".format(clueValue["clueSlider/proximityRange"]) #dispaly color text proximity with its format range value in data 6
    clue_data[7].text = "Color: R:{}G:{}B:{}C:{}".format(*(clueValue["clueSlider/colorRRange"], clueValue["clueSlider/colorGRange"], clueValue["clueSlider/colorBRange"], clueValue["clueSlider/colorCRange"])) #display sky color text accel with its specific R,B,C range value in data 7
    clue_data.show()
    

clueData = {
    "clueSlider/accelXRange" : 0, #setting the clueSlider/accelXRange equivalent to zero
    "clueSlider/accelYRange" : 0, #setting the clueSlider/accelYRange equivalent to zero
    "clueSlider/accelZRange" : 0, #setting the clueSlider/accelZRange equivalent to zero
    "clueSlider/gyroXRange" : 0,  #setting the clueSlider/gyroXRange equivalent to zero
    "clueSlider/gyroYRange" : 0,  #setting the clueSlider/gyroYRange equivalent to zero
    "clueSlider/gyroZRange" : 0,  #setting the clueSlider/gyroZRange equivalent to zero
    "clueSlider/magneticXRange" : 0,  #setting the clueSlider/magneticXRange equivalent to zero
    "clueSlider/magneticYRange" : 0,  #setting the clueSlider/magneticYRange equivalent to zero
    "clueSlider/magneticZRange" : 0,  #setting the clueSlider/magneticZRange equivalent to zero
    "clueSlider/pressureRange" : clue.pressure, # displays the current barometric pressure as well as the last two readings
    "clueSlider/tempRange" : clue.temperature,  # display the current temperature
    "clueSlider/humidityRange" : clue.humidity, # display the current humidity
    "clueSlider/proximityRange" : clue.proximity, # display the current proximity
    "clueSlider/colorRRange" : 0,  #setting the clueSlider/colorRRange equivalent to zero
    "clueSlider/colorGRange" : 0,  #setting the clueSlider/colorRRange equivalent to zero
    "clueSlider/colorBRange" : 0,  #setting the clueSlider/colorBRange equivalent to zero
    "clueSlider/colorCRange" : 0   #setting the clueSlider/colorCRange equivalent to zero
}


def on_connect(client, userdata, flags, rc): #to have a connection
    if rc == 0: #and if rc equals to 0
        client.subscribe("clueSlider/#") #subscribe to clueSlider/#
        display_text(clueData) #display all text data

def on_message(client, userdata, msg): #to connect message
    print(msg.topic) #print topic message
    print(msg.payload.decode()) #print the payload and decode message
    clueData[msg.topic]= msg.payload.decode()
    display_text(clueData)

clue_data = clue.simple_text_display(text_scale=2) #default scale of the text

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.eclipseprojects.io", 1883, 60) #connectors

client.loop_forever() #loop forever