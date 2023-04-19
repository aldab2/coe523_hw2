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

# while True:
#     for sample in range(10):
#         # conn = sqlite3.connect("example.db")
#         # c = conn.cursor()
#         c.execute('insert into READINGS VALUES (' + str(sample) + ',' + str(sample) + ',' + str(sample)  + ',' +str(sample)   + ',' + str(sample)   + ',' + str(sample)  + ')')
#         conn.commit()

conn = sqlite3.connect('example.db')
c = conn.cursor()
x = c.execute("select * from READINGS")
a = x.fetchall()
print(a)
conn.close()
