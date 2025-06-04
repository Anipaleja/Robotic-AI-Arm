from adafruit_servokit import ServoKit

# index = 0
# thumb = 2
# ring = 4
# pinky = 10
# middle = 14
kit = ServoKit(channels=16)

while True:
    # p=input('pin: ')
    pin = input("pin: ")
    angle = input("value: ")

    kit.servo[int(pin)].angle = int(angle)
