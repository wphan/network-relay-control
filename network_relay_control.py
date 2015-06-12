#!/usr/bin/env python

""" This Python script controls the network connected SainSmart 16 relay board with SainSmart Ethernet control module

    relays are toggled by fetching the following URL's
    http://192.168.1.4/30000/00: relay 1 OFF
                         .../01: relay 1 ON
                         .../02: relay 2 OFF
                         .../03: relay 2 ON
                         .../04: relay 3 OFF
                         .../05: relay 3 ON
                            .        .
                            .        .
                            .        .
                   .../toggleID: relay x 
                         OFFid = 2x-2; id for turning relay x off
                         ONid  = 2x-1; id for turning relay x on
"""
import urllib2
import os
from time import sleep

#this is the IP address of the SainSmart Relay Board
url = "http://192.168.1.4/30000"

states = ["OFF", "OFF", "OFF", "OFF", "OFF", "OFF", "OFF", "OFF", "OFF", "OFF", "OFF", "OFF", "OFF", "OFF", "OFF", "OFF"]  

def printStates():
    os.system('clear')
    print "==================================================="
    print "==  SainSmart Network Attached 16 Relay Control  =="
    print "==  NOTE: initial states are not known, toggle   =="
    print "==        all relays ON or OFF first             =="
    print "==================================================="
    print "IP address: " + url
    print ""
    for i in range(0,15):
        j = str(i + 1)
        if int(j) < 10:
           j = "0" + j 

        print "Relay: " + j + ": " + states[i]

def toggleRelay(relay):

    if states[relay-1] == "OFF":
        toggleID = str(2 * relay - 1)
        if int(toggleID) < 10:
            toggleID = "/0" + toggleID
        else:
            toggleID = "/" + toggleID

        urllib2.urlopen(url+toggleID)
        states[relay-1] = "ON"
        printStates()

    elif states[relay-1] == "ON":
        toggleID = str(2 * relay - 2)
        if int(toggleID) < 10:
            toggleID = "/0" + toggleID
        else:
            toggleID = "/" + toggleID

        urllib2.urlopen(url+toggleID)
        states[relay-1] = "OFF"
        printStates()

def toggleON():
    i = 0
    for i in range(1,17):
        toggleID = str(2 * i - 1)
        if int(toggleID) < 10:
            toggleID = "/0" + toggleID
        else:
            toggleID = "/" + toggleID
        urllib2.urlopen(url+toggleID)
        states[i-1] = "ON"
        printStates()

def toggleOFF():
    i = 0
    for i in range(1,17):
        toggleID = str(2 * i - 2)
        if int(toggleID) < 10:
            toggleID = "/0" + toggleID
        else:
            toggleID = "/" + toggleID
        urllib2.urlopen(url+toggleID)
        states[i-1] = "OFF"
        printStates()


if __name__ == "__main__":
    quit = 0
    while (quit == 0):
        printStates()
        print "Enter 'OFF' to turn all relays off, OR"
        print "Enter 'ON' to turn all relays on, OR"
        print "Enter relay number (1-16) to toggle, OR"
        choice = raw_input("Enter q to quit: ")

        if (choice == 'OFF'):
            toggleOFF()
        elif (choice == 'ON'):
            toggleON()
        elif (choice == 'q'):
            print "bye"
            break
        else:
            try: 
                int(choice)
            except ValueError:
                print "Bad command, quitting..."
                break
            else:
                if (int(choice) >= 1 and int(choice) <= 16):
                    toggleRelay(int(choice))
                else:
                    print "Bad command, quitting..."
                    break

