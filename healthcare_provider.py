###############################################################################
# (c) 2005-2015 Copyright, Real-Time Innovations.  All rights reserved.       #
# No duplications, whole or partial, manual or electronic, may be made        #
# without express written permission.  Any such copies, or revisions thereof, #
# must display this notice unaltered.                                         #
# This code contains trade secrets of Real-Time Innovations, Inc.             #
###############################################################################

from __future__ import print_function

# Updating the system path is not required if you have pip-installed
# rticonnextdds-connector
from sys import path as sys_path
from os import path as os_path
file_path = os_path.dirname(os_path.realpath(__file__))
sys_path.append(file_path + "/../../../")

import rticonnextdds_connector as rti

with rti.open_connector(
        config_name="MyParticipantLibrary::HealthcareProviderParticipant",
        url=file_path + "/VitalSigns.xml") as connector:

    input = connector.get_input("HealthcareProviderSubscriber::VitalSign")

    print("Waiting for publications...")
    input.wait_for_publications() # wait for at least one matching publication

    print("Waiting for data...")
    while True:
        input.wait() # wait for data on this input
        input.take()
        for sample in input.samples.valid_data_iter:
            print("Received {} ".format(sample.get_dictionary()))
