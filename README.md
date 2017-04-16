# traffic-build
A Raspberry Pi based build monitoring system

## Required Components

### Raspberry Pi Zero W
![Raspberry Pi Zero W](https://www.modmypi.com/image/cache/data/rpi-products/raspberry-pi-zero/w/DSC_1006-536x408.jpg)

https://www.modmypi.com/raspberry-pi/raspberry-pi-zero-board/rpi-zero-board/raspberry-pi-zero-wireless

The specific model of Raspberry Pi is mostly irrelevant. I've chosen the Zero W for its small form factor and out-of-the-box connectivity options, requiring less wiring for administration.


### ModMyPi PiOT Relay Board
![ModMyPi PiOT Relay Board](https://www.modmypi.com/image/cache/data/rpi-products/breakout-boards/modmypi/relay/DSC_0860-536x408.jpg)

https://www.modmypi.com/raspberry-pi/breakout-boards/modmypi/modmypi-piot-relay-board

The lights will run off a standard 240v 3-pin lead. That kind of voltage would kill the Pi, so a relay is used to separate the micro-controller power circuit from the light power circuit. A Relay is a switch, controlled by the GPIO pins on the Pi, allowing the Pi to turn on and off the lights.

This board is particularly nice as the Pi Zero W can mount directly on top of it!

As this board will be dealing with life-threatening amount of current, safety is paramount. The unit will be encased in an insulated enclosure before any power is passed through the relay switches.

https://www.modmypi.com/raspberry-pi/raspberry-pi-zero-board/rpi-zero-cases/modmypi-piot-relay-board-case-pi-zero

![ModMyPi PiOT Relay Board Case](https://www.modmypi.com/image/cache/data/rpi-products/cases/modmypi/piot/relay/DSC_0003-536x408.jpg)

### Raspberry Pi Zero Male Header - 40 Pin (2 x 20)
![Raspberry Pi Zero Male Header](https://www.modmypi.com/image/cache/data/electronics/headers/40x2/DSC_0186-536x408.jpg)

https://www.modmypi.com/raspberry-pi/raspberry-pi-zero-board/rpi-zero-accessories/zero-male-header-40-pin-2-x-20/

The Raspberry Pi Zero series doesn't come with any GPIO pins, only holes. This header will be soldered to the Pi Zero W and will allow it to easily slot into the GPIO ports on the relay board.

### M2.5 Mounting Screws and Nuts
![Mounting Screws](https://www.modmypi.com/image/cache/data/rpi-products/hacking-and-prototyping/screws-nuts-and-bolts/DSC_0193-536x408.jpg)

https://www.modmypi.com/electronics/screw-nuts-and-bolts/nylon-slotted-cheese-head-screws-m2.5-x-20mm

![Nuts](https://www.modmypi.com/image/cache/data/rpi-products/hacking-and-prototyping/screws-nuts-and-bolts/DSC_0194-536x408.jpg)

https://www.modmypi.com/electronics/screw-nuts-and-bolts/nylon-nut-m2.5

These are to more securely mount the Pi Zero W to the relay board.
