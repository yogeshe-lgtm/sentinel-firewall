"""
Sentinel Firewall
Logging Module

Stores firewall security events.
"""

import logging
import os


LOG_DIRECTORY = "logs"

LOG_FILE = "logs/firewall.log"



# Create log directory

if not os.path.exists(LOG_DIRECTORY):

    os.makedirs(LOG_DIRECTORY)



logging.basicConfig(

    filename=LOG_FILE,

    level=logging.INFO,

    format="%(asctime)s | %(message)s"

)



def write_log(message):

    """
    Write security event
    """

    logging.info(message)
