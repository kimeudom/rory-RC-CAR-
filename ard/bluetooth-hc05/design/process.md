# Setting up the HC05 Bluetooth Module

Refer to this youtube link for a quick explanation
```
https://youtu.be/ykgt4v7_4y4?si=ZMpXq8x5zJAIlrL7
```

The **hc-05_configurator.ino** file sets up the bluetooth module to configuration mode, it is there I changed the name and the pin to connect to the module

Configuration mode is also known as ATTENTION MODE OR *AT* MODE for short
All configuration commands are prefixed by this word

```
AT
AT+NAME=RORY_BT

```

# Post setup
After setting up the module, the basic bluetooth setup waiting for commands has been developed