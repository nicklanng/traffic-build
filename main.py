#!/usr/bin/env python

# import modules
import time
import xml.etree.ElementTree as etree
import requests
import RPi.GPIO as GPIO

# consts
BUILD_STATUS_SUCCESS = 0
BUILD_STATUS_FAILURE = 1
BUILD_STATUS_UNKNOWN = 2
PIN_RED = 5
PIN_AMBER = 6
PIN_GREEN = 16
CCNET_URL = 'http://buildservermk2/ccnet/XmlStatusReport.aspx'

# setup pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_RED, GPIO.OUT)
GPIO.setup(PIN_AMBER, GPIO.OUT)
GPIO.setup(PIN_GREEN, GPIO.OUT)

def getBuildStatus():
    r = requests.get(CCNET_URL, timeout=4)
    if r.status_code != 200:
        return BUILD_STATUS_UNKNOWN
    else:
        return parseResult(r.text)

def parseResult(text):
    root = etree.fromstring(text)
    buildStatus = BUILD_STATUS_SUCCESS
    for child in root:
        lastBuildState = child.attrib['lastBuildStatus']
        if lastBuildState == 'Failure':
            buildStatus = BUILD_STATUS_FAILURE
            break
    return buildStatus

def switchLights(buildStatus):
    if buildStatus == BUILD_STATUS_SUCCESS:
        GPIO.output(PIN_RED, GPIO.LOW)
        GPIO.output(PIN_AMBER, GPIO.LOW)
        GPIO.output(PIN_GREEN, GPIO.HIGH)
    elif buildStatus == BUILD_STATUS_UNKNOWN:
        GPIO.output(PIN_RED, GPIO.LOW)
        GPIO.output(PIN_AMBER, GPIO.HIGH)
        GPIO.output(PIN_GREEN, GPIO.LOW)
    elif buildStatus == BUILD_STATUS_FAILURE:
        GPIO.output(PIN_RED, GPIO.HIGH)
        GPIO.output(PIN_AMBER, GPIO.LOW)
        GPIO.output(PIN_GREEN, GPIO.LOW)

try:
    while True:
        try:
            buildStatus = getBuildStatus()
        except:
            buildStatus = BUILD_STATUS_UNKNOWN

        switchLights(buildStatus)

        time.sleep(1)

except KeyboardInterrupt:
    print("Quitting...")

except:
    print("Other error or exception occurred!")

finally:
    GPIO.cleanup()
