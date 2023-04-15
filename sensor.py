###############################################################################
# (c) 2005-2015 Copyright, Real-Time Innovations.  All rights reserved.       #
# No duplications, whole or partial, manual or electronic, may be made        #
# without express written permission.  Any such copies, or revisions thereof, #
# must display this notice unaltered.                                         #
# This code contains trade secrets of Real-Time Innovations, Inc.             #
###############################################################################

from time import sleep

# Updating the system path is not required if you have pip-installed
# rticonnextdds-connector
from sys import path as sys_path
from sys import argv
from os import path as os_path
from random import randint
import time
file_path = os_path.dirname(os_path.realpath(__file__))
sys_path.append(file_path + "/../../../")

import rticonnextdds_connector as rti

if len(argv) != 2 and  not isinstance(argv[1],int) :
    print("Please run as follows: python senser.py <patient_id>")
    exit(-1)
id = int(argv[1])

with rti.open_connector(
        config_name="MyParticipantLibrary::SensorParticipant",
        url=file_path + "/VitalSigns.xml") as connector:

    output = connector.get_output("SensorPublisher::VitalSign")

    print("Waiting for subscriptions...")
    output.wait_for_subscriptions()

    print("Writing...")
    i=0
    while True:
        output.instance.set_number("hr",randint(60,100))
        output.instance.set_number("bp", randint(60,140))
        output.instance.set_number("o", randint(95,100))
        output.instance.set_number("id", id)
        output.instance.set_number("count", i)
        output.instance.set_number("timestamp",time.time())
        output.write()

        sleep(0.5) # Write at a rate of one sample every 0.5 seconds, for ex.
        i+=1
