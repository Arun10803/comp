
import RPi.GPIO as GPIO
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SMTP_USERNAME = 'kksupekar371121@kkwagh.edu.in'  
SMTP_PASSWORD = 'Ksupekar@2003'  
EMAIL_FROM = 'vsdhage371121@kkwagh.edu.in'  
EMAIL_TO = 'pdeep665511@gmail.com'  
EMAIL_SUBJECT = 'Object Detected!'


IR_SENSOR_PIN = 7
LED_PIN = 11


GPIO.setmode(GPIO.BOARD)
GPIO.setup(IR_SENSOR_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)

def send_email():
    try:
        # Create a secure SSL context
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)

        # Email content
        message = MIMEMultipart()
        message['From'] = EMAIL_FROM
        message['To'] = EMAIL_TO
        message['Subject'] = EMAIL_SUBJECT
        body = "An object has been detected by the IR sensor."
        message.attach(MIMEText(body, 'plain'))

        # Send email
        server.sendmail(EMAIL_FROM, EMAIL_TO, message.as_string())

        # Clean up
        server.quit()
        print("Email sent successfully!")

    except Exception as e:
        print(f"Failed to send email: {e}")

try:
    while True:
        if GPIO.input(IR_SENSOR_PIN) == GPIO.LOW:
            print("Object detected!")
            GPIO.output(LED_PIN, GPIO.HIGH)  # Turn on LED
            send_email()  # Send email notification
            time.sleep(1)  # Delay to avoid multiple emails in quick succession
        else:
            print("No object detected.")
            GPIO.output(LED_PIN, GPIO.LOW)  # Turn off LED
       
        time.sleep(0.5)

except KeyboardInterrupt:
    print("\nExiting program.")
finally:
    GPIO.cleanup()


'''
This Python code is designed to run on a Raspberry Pi and uses an IR sensor to detect objects and trigger certain actions, such as turning on an LED and sending an email notification. Let's break down each part of the code:

Imports:
python
Copy code
import RPi.GPIO as GPIO
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
RPi.GPIO: Used to interact with the GPIO pins of the Raspberry Pi (General Purpose Input/Output).
time: Provides time-related functions, such as pausing the program for a specific amount of time (sleep).
smtplib: Used to send emails through an SMTP server.
email.mime.multipart and email.mime.text: Used to construct the email content, including the body and subject.
Email Setup:
python
Copy code
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SMTP_USERNAME = 'kksupekar371121@kkwagh.edu.in'  
SMTP_PASSWORD = 'Ksupekar@2003'  
EMAIL_FROM = 'vsdhage371121@kkwagh.edu.in'  
EMAIL_TO = 'pdeep665511@gmail.com'  
EMAIL_SUBJECT = 'Object Detected!'
SMTP_SERVER: The address of the Gmail SMTP server used to send emails.
SMTP_PORT: Port used for secure email transmission (587 for TLS).
SMTP_USERNAME: Your email address for sending the email.
SMTP_PASSWORD: Your email password (to authenticate with the SMTP server).
EMAIL_FROM: The email address that will appear as the sender.
EMAIL_TO: The email address to receive the notification.
EMAIL_SUBJECT: The subject line of the email.
Important Note: It's unsafe to hard-code your email password directly in the code. Consider using environment variables or a more secure method to store sensitive data.

IR Sensor and LED Setup:
python
Copy code
IR_SENSOR_PIN = 7
LED_PIN = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(IR_SENSOR_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)
IR_SENSOR_PIN = 7: Sets up GPIO pin 7 to read input from the IR sensor.
LED_PIN = 11: Sets up GPIO pin 11 to control the LED (turn it on or off).
GPIO.setmode(GPIO.BOARD): Uses the physical pin numbers (BOARD mode) to reference GPIO pins.
GPIO.setup(IR_SENSOR_PIN, GPIO.IN): Configures the IR sensor pin as an input pin (to detect the presence of an object).
GPIO.setup(LED_PIN, GPIO.OUT): Configures the LED pin as an output pin (to turn the LED on or off).
Email Sending Function:
python
Copy code
def send_email():
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()  # Start TLS encryption for secure communication
        server.login(SMTP_USERNAME, SMTP_PASSWORD)  # Log in to the SMTP server

        # Email content
        message = MIMEMultipart()
        message['From'] = EMAIL_FROM
        message['To'] = EMAIL_TO
        message['Subject'] = EMAIL_SUBJECT
        body = "An object has been detected by the IR sensor."
        message.attach(MIMEText(body, 'plain'))

        # Send email
        server.sendmail(EMAIL_FROM, EMAIL_TO, message.as_string())
        server.quit()  # Close the connection to the SMTP server

        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")
server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT): Creates an SMTP connection to the Gmail server.
server.starttls(): Secures the connection using TLS (Transport Layer Security).
server.login(SMTP_USERNAME, SMTP_PASSWORD): Logs into the Gmail account using the provided username and password.
MIMEMultipart(): Creates an email with multiple parts, allowing for a subject, body, and other attachments.
MIMEText(body, 'plain'): Sets the body of the email as plain text.
server.sendmail(): Sends the email.
server.quit(): Terminates the connection to the email server after the email is sent.
Main Program Loop:
python
Copy code
try:
    while True:
        if GPIO.input(IR_SENSOR_PIN) == GPIO.LOW:
            print("Object detected!")
            GPIO.output(LED_PIN, GPIO.HIGH)  # Turn on LED
            send_email()  # Send email notification
            time.sleep(1)  # Delay to avoid multiple emails in quick succession
        else:
            print("No object detected.")
            GPIO.output(LED_PIN, GPIO.LOW)  # Turn off LED
        
        time.sleep(0.5)  # Small delay to improve responsiveness
while True:: An infinite loop that continuously checks for objects detected by the IR sensor.
GPIO.input(IR_SENSOR_PIN): Reads the value from the IR sensor. When the sensor detects an object, it returns LOW, otherwise HIGH.
If an object is detected (GPIO.LOW):
print("Object detected!"): Prints a message to the console.
GPIO.output(LED_PIN, GPIO.HIGH): Turns on the LED.
send_email(): Calls the send_email() function to send the email notification.
time.sleep(1): Pauses the program for 1 second to prevent multiple email notifications from being sent in quick succession.
If no object is detected (GPIO.HIGH):
print("No object detected."): Prints a message to the console.
GPIO.output(LED_PIN, GPIO.LOW): Turns off the LED.
time.sleep(0.5): Adds a small delay to prevent the program from continuously checking the sensor too fast.
Exception Handling and Cleanup:
python
Copy code
except KeyboardInterrupt:
    print("\nExiting program.")
finally:
    GPIO.cleanup()
except KeyboardInterrupt:: Allows the program to be stopped safely using Ctrl+C (a keyboard interrupt). It prints a message and exits the program gracefully.
finally:: Ensures that the GPIO pins are cleaned up (reset to their default state) when the program ends, to avoid leaving them in an undefined state.
Summary of Functionality:
The program continuously monitors the IR sensor for an object.
If an object is detected:
It turns on an LED to indicate detection.
It sends an email notifying a user about the detection.
The program runs indefinitely, checking the IR sensor, turning the LED on/off, and sending emails when needed, until the user interrupts the program.
This code is useful in scenarios where you want to detect an object and send an immediate email alert, such as in a simple security system or monitoring application.
'''