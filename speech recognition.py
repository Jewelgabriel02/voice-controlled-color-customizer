import speech_recognition as sr
import serial
import time

# Initialize the recognizer
r = sr.Recognizer()

# Initialize serial communication (adjust COM port and baud rate as per your hardware configuration)
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
time.sleep(2)  # Wait for the connection to establish

def send_data_to_hardware(data):
    """Send data to the hardware and wait for acknowledgment."""
    ser.write(data.encode())  # Send data over serial
    print(f"Sent to hardware: {data}")
# Wait for acknowledgment
    while True:
        ack = ser.readline().decode().strip()
        if ack:
            print(f"Acknowledgment received: {ack}")
            if "Successfully pumped paint" in ack:
                break

# Predefined color values
preset_colors = {
    “indigo blue": ["red:10", "green:5", "blue:20"],
    “light blue": ["red:5", "green:15", "blue:5"],
    “Lavender purple": ["red:12", "green:3", "blue:18"],
    “warm big": ["red:8", "green:5", "blue:3"],
    “rose pink": ["red:18", "green:5", "blue:3"]
}

while True:
    try:
# Use the microphone as the source for input
        with sr.Microphone() as source2:
            # Adjust for ambient noise
            r.adjust_for_ambient_noise(source2, duration=0.2)

            # Listen for user input
            print("Listening...")
            audio2 = r.listen(source2)

            # Recognize audio using Google Speech Recognition
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
            print("Did you say:", MyText)

            # Check for preset commands (1-5)
            if MyText in preset_colors:
                for color_data in preset_colors[MyText]:
                    send_data_to_hardware(color_data)
                continue
# Parse the spoken input for red, green, and blue values
            colors = ["red", "green", "blue"]
            for color in colors:
                if color in MyText:
                    try:
                        value = int(MyText.split(color)[1].strip().split()[0])
                        data = f"{color}:{value}"
                        send_data_to_hardware(data)
                    except (IndexError, ValueError):
                        print(f"Could not parse value for {color}.")

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except sr.UnknownValueError:
        print("Unknown error occurred")
    except KeyboardInterrupt:
        print("Exiting...")
        break

ser.close()

