import bluetooth
import time

# MAC address of the HC-05 Bluetooth module
hc05_address = 'XX:XX:XX:XX:XX:XX'  # Replace with the MAC address of your HC-05 module

def send_instruction(instruction):
    sock.send(instruction)
    print(f"Sent instruction: {instruction}")

try:
    print("Connecting to HC-05...")
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    sock.connect((hc05_address, 1))
    print("Connected to HC-05")

    instructions = ["forward", "left", "right", "stop"]

    for instruction in instructions:
        send_instruction(instruction)
        time.sleep(2)  # Adjust the delay as needed

    print("Instructions sent. Closing connection.")
    sock.close()
except bluetooth.BluetoothError as e:
    print(f"Error: {e}")
