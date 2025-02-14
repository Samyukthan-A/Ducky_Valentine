# Ducky_Valentine
A Pico Ducky payload that executes a Valentine-themed Python script on the target machine. The script displays a pop-up asking the recipient out. 
If they decline multiple times ("No"), the script humorously increases the "threat level" by doing progressively and in the end can destroy the OS 

Adafruit CircuitPython contains a library that allows the Raspberry Pi Pico to be emulated as a HID (Human Interface Device).
Using Dbisu's Python script, we can use any Ducky Script, as it converts Ducky Script to run in CircuitPython.
In this version of the payload, the script is used to turn off Windows Defender and download an .exe file from the internet, "Happy Valentine.exe."
The script automatically runs the executable, which pops up a GUI asking the target to be their Valentine.
STEPS:
1.Install Adafruit CircuitPython and flash it to your Pico.
2.Copy the lib from dibisu into circuitpython(pico)
2.Copy the .py files from Dbisu's pico-ducky repository into Adafruit CircuitPython pico.
3.Rename payload.txt to .dd and upload it to the Pico running CircuitPython.
WARNING: The commented-out code in "Happy Valentine" is just to demonstrate how powerful this can be.
(I have taken extra measures to ensure it cannot be run by mistake by removing parts of the code and intentionally creating errors.)
Use this at your own risk.
