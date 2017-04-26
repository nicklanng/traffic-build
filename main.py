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
BUILD_ACTIVITY_SLEEPING = 0
BUILD_ACTIVITY_BUILDING = 1
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

def parseStatus(root):
    buildStatus = BUILD_STATUS_SUCCESS
    for child in root:
        if child.attrib['name'] not in ['Call Centre CI Build', 'Call Centre Installer Build'] :
            continue
        lastBuildState = child.attrib['lastBuildStatus']
        if lastBuildState == 'Failure':
            buildStatus = BUILD_STATUS_FAILURE
            break
    return buildStatus

def parseActivity(root):
    activity = BUILD_ACTIVITY_SLEEPING
    
    for child in root:
        if child.attrib['name'] not in ['Call Centre CI Build', 'Call Centre Installer Build'] :
            continue
        activity = child.attrib['activity']
        if activity == 'Building':
            activity = BUILD_ACTIVITY_BUILDING
            break
    return activity

def parseResult(text):
    root = etree.fromstring(text)
    buildStatus = parseStatus(root)
    activity = parseActivity(root)
    return (buildStatus, activity)

def switchStatusLights(buildStatus):
    if buildStatus == BUILD_STATUS_SUCCESS:
        GPIO.output(PIN_RED, GPIO.LOW)
        GPIO.output(PIN_GREEN, GPIO.HIGH)
    elif buildStatus == BUILD_STATUS_UNKNOWN:
        GPIO.output(PIN_RED, GPIO.HIGH)
        GPIO.output(PIN_GREEN, GPIO.HIGH)
    elif buildStatus == BUILD_STATUS_FAILURE:
        GPIO.output(PIN_RED, GPIO.HIGH)
        GPIO.output(PIN_GREEN, GPIO.LOW)

def switchActivityLights(buildStatus):
    if buildStatus == BUILD_ACTIVITY_SLEEPING:
        GPIO.output(PIN_AMBER, GPIO.LOW)
    elif buildStatus == BUILD_ACTIVITY_BUILDING:
        GPIO.output(PIN_AMBER, GPIO.HIGH)

try:
    while True:
        try:
            (buildStatus, activity) = getBuildStatus()
        except:
            buildStatus = BUILD_STATUS_UNKNOWN
            activity = BUILD_ACTIVITY_SLEEPING

        switchStatusLights(buildStatus)
        switchActivityLights(activity)

        time.sleep(1)

except KeyboardInterrupt:
    print("Quitting...")

except:
    print("Other error or exception occurred!")

finally:
    GPIO.cleanup()
