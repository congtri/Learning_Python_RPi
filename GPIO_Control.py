#!/usr/bin/python
import argparse
import RPi.GPIO as GPIO

# Define GPIO pin on Rasberry Pi board
GPIO_GEN_CH = {'gpio_gen_0': 17,  # GPIO_GEN0, BCM pin 17
               'gpio_gen_1': 18,  # GPIO_GEN1, BCM pin 18
               'gpio_gen_2': 27,  # GPIO_GEN2, BCM pin 27
               'gpio_gen_3': 22,  # GPIO_GEN3, BCM pin 22
               'gpio_gen_4': 23,  # GPIO_GEN4, BCM pin 23
               'gpio_gen_5': 24,  # GPIO_GEN5, BCM pin 24
               'gpio_gen_6': 25}  # GPIO_GEN6, BCM pin 25

parser = argparse.ArgumentParser(description='Testing')
parser.add_argument('-gpio',
                    help='Setting output status of GPIO\'s pins\n'
                         'Example:\n'
                         '\t-gpio set gpio_gen_0 or -gpio set gpio_gen_0 gpio_gen_1 ...',
                    action='store',
                    nargs='+')

arg = 0
try:
    arg = parser.parse_args()
except:
    print 'Incorrect argument'
    exit(-1)


def processInputArguments():
    # argument: -gpio set/get gpio_gen_1 gpio_gen_2
    if arg.gpio:
        # print arg.gpio
        toggle = False
        set_status = False
        if len(arg.gpio) >= 2:
            if arg.gpio[0] == 'set':
                set_status = True
            elif arg.gpio[0] == 'clear':
                set_status = False
            elif arg.gpio[0] == 'toggle':
                toggle = True
                pass
            else:
                print "incorrect argument"
                exit(-1)

            for i in range(1, len(arg.gpio), 1):
                key = arg.gpio[i]
                if GPIO_GEN_CH.has_key(key):
                    # get pin number in GPIO_GEN_CH dictionary
                    gpio_pin = GPIO_GEN_CH.get(key)
                    # Setting RPi GPIO running in BCM mode
                    GPIO.setwarnings(False)
                    GPIO.setmode(GPIO.BCM)
                    # Setting gpio_pin as output
                    GPIO.setup(gpio_pin, GPIO.OUT)
                    # Setting output status of RPi's GPIO
                    if toggle:
                        output_status = GPIO.input(gpio_pin)
                        set_status = output_status ^ toggle

                    GPIO.output(gpio_pin, set_status)
                    print "Setting", key, '- BCM PIN [', gpio_pin, ']', ' Status: ', set_status
                else:
                    print 'gpio argument: [', key, '] is incorrect'
                    exit(-1)

        else:
            print 'gpio argument incorrect'
            exit(-1)


def initGPIOOutput():
    for gpio_gen in GPIO_GEN_CH:
        gpio_pin_num = GPIO_GEN_CH.get(gpio_gen)
        print gpio_gen, 'PIN[', gpio_pin_num, ']'
        GPIO.setup(gpio_pin_num, GPIO.OUT)


if __name__ == '__main__':
    # GPIO.setmode(GPIO.BCM)
    # initGPIOOutput()
    processInputArguments()
    pass

