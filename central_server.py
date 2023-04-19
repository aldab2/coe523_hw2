###############################################################################
# (c) Copyright, Real-Time Innovations, 2019.  All rights reserved.           #
# No duplications, whole or partial, manual or electronic, may be made        #
# without express written permission.  Any such copies, or revisions thereof, #
# must display this notice unaltered.                                         #
# This code contains trade secrets of Real-Time Innovations, Inc.             #
###############################################################################

"""Reads Squares, transforms them and writes them as Circles."""

from sys import path as sys_path
from os import path as os_path
import logging
from logging.handlers import TimedRotatingFileHandler
import sqlite3
conn = sqlite3.connect("readings.db")
c = conn.cursor()
c.execute('create table if not EXISTS READINGS (id int, hr int, bp int, o int, count int, timestamp int)')
conn.commit()

def init_logger():
    logger = logging.getLogger("sensor_data.log")
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter(
        fmt='%(asctime)s ~ %(levelname)s ~ %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S')

    fh = TimedRotatingFileHandler("sensor_data.log", when="M", interval=5,backupCount=7)
    fh.setFormatter(formatter)
    fh.suffix = "%Y-%m-%d_%H-%M-%S"
    logger.addHandler(fh)
    return logger



file_path = os_path.dirname(os_path.realpath(__file__))
sys_path.append(file_path + "/../../../")
import rticonnextdds_connector as rti

logger = init_logger()
with rti.open_connector(
        config_name="MyParticipantLibrary::CentralServerParticipant",
        url=file_path + "/VitalSigns.xml") as connector:

    input = connector.get_input("CentralServerSubscriber::VitalSign")
    output = connector.get_output("CentralServerPublisher::VitalSign")

    # Read data from the input, transform it and write it into the output
    print("Waiting for data...")
    while True:
        input.wait() # Wait for data in the input
        input.take()
        for sample in input.samples.valid_data_iter:
            data : dict() = sample.get_dictionary()
            logger.info(str(data))
            c.execute('insert into READINGS VALUES (' + str(data['id']) + ',' + str(data['hr']) + ',' + str(data['bp']) + ',' + str(data['o']) + ',' + str(data['count'])  + ',' + str(data['timestamp']) + ')')
            conn.commit()
            print("Reveiced {}".format(str(data)))
            output.instance.set_dictionary(data)
            output.write()

