# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 23:41:59 2018

@author: Jonas Lindemann
"""

import logging

def do_some_logging():
    logging.debug("Detta är ett testmeddelande...")
    logging.info("Detta är ett informationsmeddelande...")
    logging.warning("Detta är en varning...")
    logging.error("Detta är ett felmeddelande...")
    logging.critical("Detta är ett kritiskt fel...")

logging.basicConfig(level=logging.DEBUG)

do_some_logging()

logging.getLogger().setLevel(logging.ERROR)

do_some_logging()
